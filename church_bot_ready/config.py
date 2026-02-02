from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str
    PRAYER_CHAT_ID: int
    CARE_CHAT_ID: int
    YOUTH_CHAT_ID: int

config = Config(
    BOT_TOKEN=os.getenv('BOT_TOKEN'),
    PRAYER_CHAT_ID=int(os.getenv('PRAYER_CHAT_ID')),
    CARE_CHAT_ID=int(os.getenv('CARE_CHAT_ID')),
    YOUTH_CHAT_ID=int(os.getenv('YOUTH_CHAT_ID')),
)
