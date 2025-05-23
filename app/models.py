from pydantic import BaseModel
from datetime import datetime

class PostRequest(BaseModel):
    platform: str
    post_text: str

class ReplyResponse(BaseModel):
    generated_reply: str
    timestamp: datetime
