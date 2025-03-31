import re
from typing import List
from idt_scrapper.domain.scanners.promo_scanner_interface import PromoScannerInterface
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.entities.promo import Promo

class PromoScanner(PromoScannerInterface):
    def scan_promos(self, content: List[Content]) -> List[Promo]:
        promos = []

        for _content in content:
            promos = self.get_sentences_with_links(_content.description)
            # get tags from links
            # insert into promos
        
        return promos

    def get_sentences_with_links(self, description: str) -> List[Promo]:
        # Regex pattern for URLs
        url_pattern = r'https?://\S+|www\.\S+'
        
        # Split text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', description)
        
        # Filter sentences that contain a URL
        sentences_with_links = [sentence for sentence in sentences if re.search(url_pattern, sentence)]
        
        return sentences_with_links
