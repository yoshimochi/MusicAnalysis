import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import get_track, create_music_data

def main(spotipy, playlist_ids):
    # csvに出力するために分析対象の曲のIDを取得する
    track_ids: list = list(get_track.getTrackIDs(spotipy, playlist_ids))

    # csvファイルとして出力
    music_data = create_music_data.create_csv(spotipy, track_ids)

    # csvディレクトリに保存
    music_data.to_csv('csv/spotify_music_data.csv', sep=',')

client_credentials_manager = SpotifyClientCredentials(config.SPOTIPY_CLIENT_ID, config.SPOTIPY_CLIENT_SECRET)
spotipy = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlist_ids = ['42vVvTztB8SlSM4Lnk5IZQ', '3NTFAftiUeEgmC8VoOLdJ7', '64RyuP5abUN6U5XjmqOOD4']

main(spotipy, playlist_ids)
