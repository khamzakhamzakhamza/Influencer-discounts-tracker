from pydantic import BaseModel

class DeleteInfluencerRequest(BaseModel):
    username: str
    influencer_id: str
