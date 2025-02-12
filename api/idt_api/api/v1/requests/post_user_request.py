from pydantic import BaseModel

class PostUserRequest(BaseModel):
    username: str