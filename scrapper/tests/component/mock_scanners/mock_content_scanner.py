from datetime import datetime, timezone, timedelta
from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.scanners.content_scanner_intrerface import ContentScannerInterface
from idt_scrapper.domain.entities.content import Content
from tests.shared.builders.content_builder import ContentBuilder

class MockContentScanner(ContentScannerInterface):
    def scan_content(self, influencer: Influencer,  cutoff_date: datetime) -> List[Content]:
        return [
            ContentBuilder().with_content_creation_date(datetime.now(timezone.utc) - timedelta(days=1)).build(),
        ]
