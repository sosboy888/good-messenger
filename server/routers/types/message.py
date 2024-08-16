from pydantic import BaseModel


class Message(BaseModel):
    user_id: str
    to_id: str
    text: str

class FetchRequest(BaseModel):
    from_id: str
    to: str