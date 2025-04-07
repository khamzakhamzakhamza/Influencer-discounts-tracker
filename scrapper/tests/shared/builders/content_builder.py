from datetime import datetime, timezone
from idt_scrapper.domain.entities.content import Content

class ContentBuilder:
    def __init__(self):
        self.id = "iMOytUm33kM"
        self.title = "Are 5 More States Getting Ranked Choice Voting?"
        self.prompt = """American voters won't just be headed to the polls this Election Day to vote for politicians. They'll also be voting to CHANGE THE LAW. 

Sources/further reading:
https://apnews.com/article/voting-immigrants-noncitizen-trump-republicans-2024-1c65429c152c2a10514b5156eacf9ca7
https://ballotpedia.org/2024_ballot_measures#Topics 

Join this channel to get access to perks:
https://www.youtube.com/channel/UCmYesELO6axBrCuSpf7S9DQ/join

For business inquiries or to send snail mail to Mr. Beat: 
https://www.iammrbeat.com/contact.html
https://www.youtube.com/c/iammrbeat/about

How to support and donate to my channel: 
Subscribe to @iammrbeat & hit the notification bell 🔔
Join for great perks on Patreon: https://www.patreon.com/iammrbeat
Donate to Mr. Beat on Paypal: https://www.paypal.me/mrbeat
Buy Mr. Beat a coffee: https://ko-fi.com/iammrbeat
Cameo: https://www.cameo.com/iammrbeat
Subscribe to my second channel: The Beat Goes On
Patreon for The Beat Goes On: https://www.patreon.com/thebeatgoeson

Connect with me:
Links: https://linktr.ee/iammrbeat
Website: https://www.iammrbeat.com/
Podcast: https://anchor.fm/thebeatpod
Reddit: https://www.reddit.com/r/mrbeat/
@beatmastermatt on Twitter: https://twitter.com/beatmastermatt
Facebook: https://www.facebook.com/iammrbeat/
Instagram: https://www.instagram.com/iammrbeat
Beatcord: https://discord.gg/g8cZPjt
TikTok: https://www.tiktok.com/@iammrbeat

Merch:
https://matt-beat-shop.fourthwall.com/
https://www.bonfire.com/store/mr-beat/
https://sfsf.shop/support-mrbeat/
https://amzn.to/3fdakiZ

There are at least 160 statewide ballot measures across 41 states in the 2024 United States elections.

11 of these measures are related to abortion, a record amount for a single year. Ten ballot measures would create state constitutional rights to have an abortion. In Nebraska, a ballot measure would limit the ability to have an abortion.

6 of these measures ban voting for people who aren’t American citizens. By the way, there’s already a voting ban on noncitizens for federal elections. 

5 of these measures would implement ranked choice voting. One would get rid of ranked choice voting in Alaska. Another would prevent ranked choice from ever happening in Missouri. 

4 raise the minimum wage. 3 legalize marijuana, including notably in Florida. Massachusetts could become the third state to legalize psychedelics. 

There’s a lot more to vote for than just the president.

#2024elections #2024election #2024uselection 

Affiliate Links: 
Useful Charts: https://usefulcharts.com/?aff=12 
Fourthwall: https://link.fourthwall.com/MrBeat
StreamYard: https://streamyard.com/pal/d/5272340869152768"""
        self.content_url = "https://www.youtube.com/watch?v=iMOytUm33kM"
        self.creation_date = datetime.now(timezone.utc)
        self.content_creation_date = datetime.now(timezone.utc)
        self.version = 1

    def with_id(self, id: str):
        self.id = id
        return self
    
    def with_title(self, title: str):
        self.title = title
        return self
    
    def with_prompt(self, prompt: str):
        self.prompt = prompt
        return self
    
    def with_content_url(self, content_url: str):
        self.content_url = content_url
        return self
    
    def with_creation_date(self, creation_date: datetime):
        self.creation_date = creation_date
        return self
    
    def with_content_creation_date(self, content_creation_date: datetime):
        self.content_creation_date = content_creation_date
        return self
    
    def with_version(self, version: int):
        self.version = version
        return self
    
    def build(self):
        return Content(self.id, self.title, self.prompt, self.content_url, self.creation_date, self.content_creation_date, self.version)
