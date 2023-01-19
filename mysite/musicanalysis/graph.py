import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns


def plot_histogram(analysis_data):
    df = analysis_data

    fig = plt.figure()

    plt.switch_backend("AGG")

    ax1 = fig.add_subplot(1, 1, 1)

    x1 = df["popularity"]
    # x2 = df["key"]
    # x3 = df["mode"]
    # x4 = df["danceability"]
    # x5 = df["acousticness"]
    # x6 = df["energy"]
    # x7 = df["instrumentalness"]
    # x8 = df["liveness"]
    # x9 = df["loudness"]
    # x10 = df["speechiness"]
    # x11 = df["tempo"]
    # x12 = df["time_signature"]

    # スコットの選択
    ax1.hist(x1, bins="auto")
    # ax2.hist(x2, bins="auto", range=(0, 1), density=True)
    # ax3.hist(x3, bins="auto", range=(0, 1), density=True)
    # ax4.hist(x4, bins="auto", range=(0, 1), density=True)
    # ax5.hist(x5, bins="auto", range=(0, 1), density=True)
    # ax6.hist(x6, bins="auto", range=(0, 1), density=True)
    # ax7.hist(x7, bins="auto", range=(0, 1), density=True)
    # ax8.hist(x8, bins="auto", range=(0, 1), density=True)
    # ax9.hist(x9, bins="auto", range=(0, 1), density=True)
    # ax10.hist(x10, bins="auto", range=(0, 1), density=True)
    # ax11.hist(x11, bins="auto", range=(0, 1), density=True)
    # ax12.hist(x12, bins="auto", range=(0, 1), density=True)

    ax1.set_title('popularity histgram')
    ax1.set_xlabel('popularity')
    ax1.set_ylabel('frequency')


def output_plot():
    buffer = BytesIO()  # バイナリI/O(画像や音声データを取り扱う際に利用)
    plt.savefig(buffer, format="svg", bbox_inches='tight')  # svg形式の画像データを取り扱う
    img = buffer.getvalue()  # バッファの全内容を含むbytes
    buffer.close()
    return img


def output_heatmap(analysis_data):
    df = analysis_data.drop(columns=['id', 'name', 'album', 'artist', 'release_date', 'length'])

    # 正規化
    df_mean = (df - df.min()) / (df.max() - df.min())
    df_mean = df_mean.corr().round(2)
    sns.heatmap(df_mean, cmap='coolwarm', vmin=-1, vmax=1, annot=True)
    plt.show()
