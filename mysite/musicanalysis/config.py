# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv

import os

load_dotenv()

# 環境変数を参照
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
