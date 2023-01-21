import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mysite import settings

csv_dir = settings.MEDIA_ROOT + "spotify_music_data.csv"
analysis_data = pd.read_csv(csv_dir, index_col=0)


def plot_histogram():
    # グラフ作成に不要な列を削除
    df = analysis_data.drop(
        columns=["name", "album", "artist", "release_date"]
    )
    columns = df.columns.values

    plt.switch_backend("AGG")
    print(analysis_data.describe())

    # 列名でループをしてグラフを作成
    for column in columns:
        plt.cla()
        plt.hist(analysis_data[column], bins="scott", range=(0, 1))

        plt.title(column + ' histgram')
        plt.xlabel(column)
        plt.ylabel("frequency")

        save_dir = "./static/png/" + column + ".png"
        plt.savefig(save_dir)


def plot_heatmap():
    df = analysis_data.drop(
        columns=["name", "album", "artist", "release_date", "length"]
    )

    # 正規化
    df_mean = (df - df.min()) / (df.max() - df.min()) * 2 + 2
    df_mean = df_mean.corr().round(2)
    matrix = np.triu(np.ones_like(df_mean))
    plt.figure(figsize=(16, 8))
    sns.heatmap(df_mean, vmin=-1, vmax=1, cmap="BrBG", annot=True, mask=matrix)
    plt.savefig("./static/png/heatmap.png")
