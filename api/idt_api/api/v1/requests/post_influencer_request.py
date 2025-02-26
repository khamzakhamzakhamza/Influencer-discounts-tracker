from pydantic import BaseModel

class PostInfluencerRequest(BaseModel):
    link: str