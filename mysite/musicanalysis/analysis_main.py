import os, sys
import pathlib
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"/../mysite/")

import pandas as pd
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from .get_track import get_track_ids, get_track_features
from .create_music_data import create_csv, to_csv
from .graph import plot_histogram, output_heatmap
from .config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from mysite import settings

def main(playlist_id):
    # Spotipy認証
    client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    spotipy = Spotify(client_credentials_manager=client_credentials_manager)

    csv_dir = settings.MEDIA_ROOT + "spotify_music_data.csv"

    # csvに出力するために分析対象の曲のIDを取得する
    track_ids: list = list(get_track_ids(spotipy, playlist_id))

    # csvに出力するために分析対象の曲のIDを取得する
    track_ids: list = list(get_track_ids(spotipy, playlist_id))

    # csvファイルとして出力
    music_data = create_csv(spotipy, track_ids)

    # csvディレクトリに保存
    to_csv(music_data)

    # 保存したcsvを読み込む
    analysis_data = pd.read_csv(csv_dir)

    # ヒストグラムを描画
    # hist = plot_histogram(analysis_data)

    # 相関関係を描画
    # output_heatmap(analysis_data)

    # csv保存ディレクトリを初期化
    # os.remove(csv_dir)

    return analysis_data



# main(spotipy, playlist_ids)

