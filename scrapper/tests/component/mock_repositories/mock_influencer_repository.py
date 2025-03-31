from typing import List
from idt_scrapper.domain.entities.influencer import Influencer
from idt_scrapper.domain.repositories.influencer_repository_interface import InfluencerRepositoryInterface

class MockInfluencerRepository(InfluencerRepositoryInterface):
    __influencers = [
        Influencer(
            'UC4EQHfzIbkL_Skit_iKt1aA',
            '@moistcharlieclipsofficial',
            'Moist Charlie Clips',
            'https://www.youtube.com/@moistcharlieclipsofficial',
            'https://yt3.ggpht.com/uNnYRnCNiXwSx3IZcJoV0fRmDlTQIsIu4rHsGWvLSjGslrv-D4m1bUO6c7-0zoU4J8ol-9OrNvo=s88-c-k-c0x00ffffff-no-rj',
            '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            '2021-09-20T19:00:00Z',
            '2021-09-20T19:00:00Z'),
        Influencer(
            'UC4EQHfzIbkL_Skit_iKt1aA',
            '@moistcharlieclipsofficial',
            'Moist Charlie Clips',
            'https://www.youtube.com/@moistcharlieclipsofficial',
            'https://yt3.ggpht.com/uNnYRnCNiXwSx3IZcJoV0fRmDlTQIsIu4rHsGWvLSjGslrv-D4m1bUO6c7-0zoU4J8ol-9OrNvo=s88-c-k-c0x00ffffff-no-rj',
            '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            '2021-09-20T19:00:00Z',
            '2021-09-20T19:00:00Z'),
        Influencer(
            'UC4EQHfzIbkL_Skit_iKt1aA',
            '@moistcharlieclipsofficial',
            'Moist Charlie Clips',
            'https://www.youtube.com/@moistcharlieclipsofficial',
            'https://yt3.ggpht.com/uNnYRnCNiXwSx3IZcJoV0fRmDlTQIsIu4rHsGWvLSjGslrv-D4m1bUO6c7-0zoU4J8ol-9OrNvo=s88-c-k-c0x00ffffff-no-rj',
            '57ae1dd2-592c-49f4-8f92-55a29a744ba2',
            '2021-09-20T19:00:00Z',
            '2021-09-20T19:00:00Z'),
    ]
    def get_influencers_by_desc_update_date(self, count: int = 100) -> List[Influencer]:        
        return self.__influencers
    
    def update_influencer(self, influencer: Influencer):
        for i, existing_influencer in enumerate(self.__influencers):
            if existing_influencer.channelId == influencer.channelId:
                self.__influencers[i] = influencer
                break
