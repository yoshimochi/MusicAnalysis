from datetime import date

import spotipy


def get_track_ids(spotipy, playlist_ids):
    track_ids = []

    for playlist_id in playlist_ids:
        playlist = spotipy.playlist(playlist_id)
        while playlist['tracks']['next']:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])
            playlist['tracks'] = spotipy.next(playlist['tracks'])
        else:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])

    return track_ids


def get_track_features(spotipy, id):
    meta = spotipy.track(id)
    features = spotipy.audio_features(id)

    name: str = meta['name']
    album: str = meta['album']['name']
    artist: str = meta['album']['artists'][0]['name']
    release_date: date = meta['album']['release_date']
    length: int = meta['duration_ms']
    popularity: int = meta['popularity']
    key: int = features[0]['key']
    mode: int = features[0]['mode']
    danceability: float = features[0]['danceability']
    acousticness: float = features[0]['acousticness']
    energy: float = features[0]['energy']
    instrumentalness: float = features[0]['instrumentalness']
    liveness: float = features[0]['liveness']
    loudness: float = features[0]['loudness']
    speechiness: float = features[0]['speechiness']
    tempo: float = features[0]['tempo']
    time_signature: int = features[0]['time_signature']
    valence: float = features[0]['valence']

    track = [name, album, artist, release_date, length, popularity, key, mode, danceability, acousticness, energy,
             instrumentalness, liveness, loudness, speechiness, tempo, time_signature, valence]
    return track
