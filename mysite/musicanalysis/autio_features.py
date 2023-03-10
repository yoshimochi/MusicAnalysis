import sys, time
import pathlib

currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir) + "/../mysite/")

import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from .get_track import get_track_ids, get_track_features
from .config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from mysite import settings


def output_csv(playlist_id):
    # Spotipy認証
    client_credentials_manager = SpotifyClientCredentials(
        SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
    )
    spotipy = Spotify(client_credentials_manager=client_credentials_manager)

    # csvに出力するために分析対象の曲のIDを取得する
    track_ids = list(get_track_ids(spotipy, playlist_id))

    # csvファイルとして出力
    music_data = create_df(spotipy, track_ids)

    # csvディレクトリに保存
    save_csv(music_data)


def create_df(spotipy, track_ids):
    tracks = []

    for track_id in track_ids:
        time.sleep(0.5)
        track = get_track_features(spotipy, track_id)
        tracks.append(track)

    df = pd.DataFrame(
        tracks,
        columns=[
            "name",
            "album",
            "artist",
            "release_date",
            "popularity",
            "danceability",
            "acousticness",
            "energy",
            "instrumentalness",
            "liveness",
            "speechiness",
            "valence",
        ],
    )
    df.head()
    return df


def save_csv(df):
    exp_path = settings.MEDIA_ROOT + "spotify_music_data.csv"
    df.to_csv(exp_path, encoding="utf-8", index=False)
    return df
