import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def output_histogram(analysis_data):
    df = analysis_data

    fig = plt.figure()
    plt.subplots_adjust(wspace=1, hspace=1)

    ax1 = fig.add_subplot(4, 4, 1)
    ax2 = fig.add_subplot(4, 4, 2)
    ax3 = fig.add_subplot(4, 4, 3)
    ax4 = fig.add_subplot(4, 4, 4)
    ax5 = fig.add_subplot(4, 4, 5)
    ax6 = fig.add_subplot(4, 4, 6)
    ax7 = fig.add_subplot(4, 4, 7)
    ax8 = fig.add_subplot(4, 4, 8)
    ax9 = fig.add_subplot(4, 4, 9)
    ax10 = fig.add_subplot(4, 4, 10)
    ax11 = fig.add_subplot(4, 4, 11)
    ax12 = fig.add_subplot(4, 4, 12)

    x1 = df["popularity"]
    x2 = df["key"]
    x3 = df["mode"]
    x4 = df["danceability"]
    x5 = df["acousticness"]
    x6 = df["energy"]
    x7 = df["instrumentalness"]
    x8 = df["liveness"]
    x9 = df["loudness"]
    x10 = df["speechiness"]
    x11 = df["tempo"]
    x12 = df["time_signature"]

    # スコットの選択
    ax1.hist(x1, bins="auto", range=(0, 1), density=True)
    ax2.hist(x2, bins="auto", range=(0, 1), density=True)
    ax3.hist(x3, bins="auto", range=(0, 1), density=True)
    ax4.hist(x4, bins="auto", range=(0, 1), density=True)
    ax5.hist(x5, bins="auto", range=(0, 1), density=True)
    ax6.hist(x6, bins="auto", range=(0, 1), density=True)
    ax7.hist(x7, bins="auto", range=(0, 1), density=True)
    ax8.hist(x8, bins="auto", range=(0, 1), density=True)
    ax9.hist(x9, bins="auto", range=(0, 1), density=True)
    ax10.hist(x10, bins="auto", range=(0, 1), density=True)
    ax11.hist(x11, bins="auto", range=(0, 1), density=True)
    ax12.hist(x12, bins="auto", range=(0, 1), density=True)

    # ax.set_title('danceability histgram')
    # ax.set_xlabel('danceability')
    # ax.set_ylabel('frequency')
    plt.show()


def output_heatmap(analysis_data):
    df = analysis_data.drop(columns=['id', 'name', 'album', 'artist', 'release_date', 'length'])
    print(df.dtypes)

    # 正規化
    df_mean = (df - df.min()) / (df.max() - df.min())
    df_mean = df_mean.corr().round(2)
    sns.heatmap(df_mean, cmap='coolwarm', vmin=-1, vmax=1, annot=True)
    plt.show()
