from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.scanners.influencer_scanner_interface import InfluencerScannerInterface

class MockInfluencerScanner(InfluencerScannerInterface):
    def rescan_influencer(self, influencer: Influencer):
        pass
