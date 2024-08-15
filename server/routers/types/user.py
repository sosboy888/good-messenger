from pydantic import BaseModel
from datetime import date
"""
uuid - Primary key
username - TEXT
password_hash - TEXT
"""

class User(BaseModel):
    username: str
    password_hash: str