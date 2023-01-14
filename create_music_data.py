import time
import pandas as pd
import get_track

def create_csv(spotipy, track_ids):
    tracks = []

    for track_id in track_ids:
        time.sleep(5)
        track = get_track.getTrackFeatures(spotipy, track_id)
        tracks.append(track)

    df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'key', 'mode',
                                   'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness',
                                   'loudness', 'speechiness', 'tempo', 'time_signature', 'valence'])

    return df
