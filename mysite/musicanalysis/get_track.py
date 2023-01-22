from datetime import date


def get_track_ids(spotipy, playlist_id):
    track_ids = []

    playlist = spotipy.playlist(playlist_id)
    while playlist["tracks"]["next"]:
        for item in playlist["tracks"]["items"]:
            track = item["track"]
            if not track["id"] in track_ids:
                track_ids.append(track["id"])
        playlist["tracks"] = spotipy.next(playlist["tracks"])
    else:
        for item in playlist["tracks"]["items"]:
            track = item["track"]
            if not track["id"] in track_ids:
                track_ids.append(track["id"])

    return track_ids


def get_track_features(spotipy, id):
    meta = spotipy.track(id)
    features = spotipy.audio_features(id)

    name: str = meta["name"]
    album: str = meta["album"]["name"]
    artist: str = meta["album"]["artists"][0]["name"]
    release_date: date = meta["album"]["release_date"]
    popularity: int = meta["popularity"]
    danceability: float = features[0]["danceability"]
    acousticness: float = features[0]["acousticness"]
    energy: float = features[0]["energy"]
    instrumentalness: float = features[0]["instrumentalness"]
    liveness: float = features[0]["liveness"]
    speechiness: float = features[0]["speechiness"]
    valence: float = features[0]["valence"]

    track = [
        name,
        album,
        artist,
        release_date,
        popularity,
        danceability,
        acousticness,
        energy,
        instrumentalness,
        liveness,
        speechiness,
        valence,
    ]
    return track
