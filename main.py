import pandas as pd

import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from mysite.musicanalysis.spotipy import analysis


def main(spotipy, playlist_ids):
    csv_dir = 'csv/spotify_music_data.csv'

    # csvに出力するために分析対象の曲のIDを取得する
    # track_ids: list = list(get_track.get_track_ids(spotipy, playlist_ids))
    #
    # # csvファイルとして出力
    # music_data = create_music_data.create_csv(spotipy, track_ids)
    #
    # # csvディレクトリに保存
    # music_data.to_csv(csv_dir, sep=',')

    # 保存したcsvを読み込む
    analysis_data = pd.read_csv(csv_dir)

    # ヒストグラムを描画
    analysis.output_histogram(analysis_data)

    # 相関関係を描画
    analysis.output_heatmap(analysis_data)

    # track_idsの初期化
    # trace_ids = []

    # csv保存ディレクトリを初期化
    # os.remove(csv_dir)


# Spotipy認証
client_credentials_manager = SpotifyClientCredentials(config.SPOTIPY_CLIENT_ID, config.SPOTIPY_CLIENT_SECRET)
spotipy = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_ids = ['42vVvTztB8SlSM4Lnk5IZQ', '3NTFAftiUeEgmC8VoOLdJ7', '64RyuP5abUN6U5XjmqOOD4']

main(spotipy, playlist_ids)
