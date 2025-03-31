from datetime import datetime, timezone, timedelta
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.entities.content import Content

class MockContentScanner(ContentScannerInterface):
    def scan_content(self, influencer: Influencer,  cutoff_date: datetime) -> List[Content]:
        current_date = datetime.now(timezone.utc)
        valid_date = current_date - timedelta(days=2)

        return [
            Content(
                '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
                'The Best Content Ever',
                'The best content ever created',
                'https://www.youtube.com/watch?v=57ae1dd2-592c-49f4-8f92-55a29a744ba2',
                current_date,
                valid_date,
            )
        ]
