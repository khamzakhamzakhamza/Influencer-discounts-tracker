import re
import uuid
import requests
import nltk
from nltk.corpus import stopwords
from datetime import datetime, timezone
from typing import Counter, List, Optional
from bs4 import BeautifulSoup
from idt_scrapper.domain.scanners.affiliated_link_scanner_interface import AffiliatedLinkScannerInterface
from idt_scrapper.domain.entities.content import Content
from idt_scrapper.domain.entities.affiliated_link import AffiliatedLink
from idt_scrapper.domain.errors.scanning_error import ScanningError

class BeautifulSoupAffiliatedLinkScanner(AffiliatedLinkScannerInterface):
    nltk.download('stopwords')
    STOP_WORDS = set(stopwords.words('english'))

    def scan_links(self, content: Content) -> List[AffiliatedLink]:
        promos = []

        links = self.get_links(content.prompt)
        promo_links = self.filter_social_media_links(links)

        for promo_link in promo_links:
            try:
                webpage = self.get_promo_webpage(promo_link)

                tokens = self.get_top_words(webpage) + self.get_meta_tags(webpage)

                affiliated_link = AffiliatedLink(
                    id =  str(uuid.uuid4()),
                    prompt= content.prompt,
                    tokens=tokens,
                    link=promo_link,
                    creation_date=datetime.now(timezone.utc),
                    version=1
                )

                promos.append(affiliated_link)
            except ScanningError as e:
                # TODO: Lgg error
                print(e)

        return promos

    def get_links(self, prompt: str) -> List[str]:
        url_pattern = r'(https?://[^\s]+|www\.[a-zA-Z0-9\-._~:/?#@!$&\'()*+,;=%]+)'
        matches = re.findall(url_pattern, prompt)
        return [match.rstrip(".,!?)") for match in matches]
    
    def filter_social_media_links(self, links: List[str]) -> List[str]:
        social_media_domains = {
            'instagram', 'tiktok', 'youtube', 'twitter', 'facebook', 'linkedin',
            'reddit', 'pinterest', 'snapchat', 'twitch', 'discord', 'patreon',
            'paypal', 'linktr', 'cameo', 'ko-fi', 'buymeacoffee'
        }

        return [
            link for link in links
            if not any(domain in link for domain in social_media_domains)
        ]

    def get_promo_webpage(self, link: str) -> Optional[BeautifulSoup]:
        response = requests.get(link)

        if not response.ok:
            raise ScanningError(link, "get_affiliated_link_fetch", Exception(response.text))

        return BeautifulSoup(response.content, 'html.parser')
    
    def get_top_words(self, webpage: BeautifulSoup) -> List[str]:
        text_content = webpage.get_text()

        words = re.findall(r'\w+', text_content.lower())
        filtered_words = [word for word in words if word not in self.STOP_WORDS]
        
        word_counts = Counter(filtered_words)

        most_common_words = word_counts.most_common(10)

        return [word for word, _ in most_common_words]
    
    def get_meta_tags(self, webpage: BeautifulSoup) -> List[str]:
        allowed_meta_keys = {
            "description",
            "og:title",
            "og:description",
            "twitter:title",
            "twitter:description",
            "keywords"
        }

        meta_values = []

        for meta in webpage.find_all("meta"):
            name = meta.get("name", "").lower()
            prop = meta.get("property", "").lower()
            content = meta.get("content", "").strip()

            if name in allowed_meta_keys or prop in allowed_meta_keys:
                if content and len(content.split()) > 2:
                    meta_values.append(content)

        return meta_values