import time, sys
import pathlib
import pandas as pd
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"/../mysite/")

from .get_track import get_track_features
from mysite import settings



def create_csv(spotipy, track_ids):
    tracks = []

    for track_id in track_ids:
        time.sleep(0.5)
        track = get_track_features(spotipy, track_id)
        tracks.append(track)

    df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'key', 'mode',
                                       'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness',
                                       'loudness', 'speechiness', 'tempo', 'time_signature', 'valence'])

    return df


def to_csv(df):
    exp_path = settings.MEDIA_ROOT + "spotify_music_data.csv"
    df.to_csv(exp_path, encoding='utf-8', index=False)
    return df
