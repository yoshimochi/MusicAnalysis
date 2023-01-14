import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def output_histogram(analysis_data):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = analysis_data["energy"]
    ax.hist(x, bins="scott", range=(0, 1))  # スコットの選択
    ax.set_title('energy histgram')
    ax.set_xlabel('popularity')
    ax.set_ylabel('frequency')
    plt.xlim(0, 1)
    plt.show()


def output_heatmap(analysis_data):
    df = analysis_data.drop(columns=['id', 'name', 'album', 'artist', 'release_date', 'length'])
    print(df.dtypes)

    # 正規化
    df_mean = (df - df.min()) / (df.max() - df.min())
    df_mean = df_mean.corr().round(2)
    sns.heatmap(df_mean, cmap='coolwarm', vmin=-1, vmax=1, annot=True)
    plt.show()
