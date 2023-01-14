import spotipy

def getTrackIDs(spotipy, playlist_ids):
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

def getTrackFeatures(spotipy, id):
    meta = spotipy.track(id)
    features = spotipy.audio_features(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    key = features[0]['key']
    mode = features[0]['mode']
    danceability = features[0]['danceability']
    acousticness = features[0]['acousticness']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    valence = features[0]['valence']

    track = [name, album, artist, release_date, length, popularity, key, mode, danceability, acousticness, energy,
             instrumentalness, liveness, loudness, speechiness, tempo, time_signature, valence]
    return track