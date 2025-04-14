from typing import List, Optional
from datetime import datetime, timedelta, timezone
from idt_scrapper.config import settings
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.repositories.content_repository_interface import ContentRepositoryInterface
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.entities.content import Content

class ContentService:
    def __init__(self, content_repository: ContentRepositoryInterface, content_scanner: ContentScannerInterface):
        self._content_repository = content_repository
        self._content_scanner = content_scanner
    
    def delete_stale(self, influencer: Influencer) -> Optional[datetime]:
        content = self._content_repository.get_content(influencer)
        cutoff_date = (datetime.now(timezone.utc) - timedelta(days=settings.CONTENT_PERIOD_DAYS)).date()

        content_to_delete = [
            _content.id
            for _content in content
            if _content.content_creation_date.date() < cutoff_date
        ]

        self._content_repository.delete_content(content_to_delete)

        if len(content) > 0:
            most_recent_content = content[0].content_creation_date.date()
            return content[0].content_creation_date if most_recent_content > cutoff_date else None
        
        return None

    def save_content(self, influencer: Influencer, cutoff_date: Optional[datetime]) -> List[Content]:
        cutoff_date = cutoff_date.date() if cutoff_date else (datetime.now(timezone.utc) - timedelta(days=settings.CONTENT_PERIOD_DAYS)).date()
        content = self._content_scanner.scan_content(influencer, cutoff_date)
        self._content_repository.save_content(influencer, content)
        return content