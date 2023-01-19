import io
import os
from urllib.parse import urlencode, urlparse
import matplotlib
# バックエンドを指定
import matplotlib.pyplot as plt
import pandas as pd

from mysite import settings

matplotlib.use('Agg')

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PlaylistIdForm
from . import analysis_main
from .models import PlaylistIdModel
from .graph import plot_histogram, output_plot


# Create your views here.
def top(request):
    if request.method == "POST":

        analysis_url = PlaylistIdForm(request.POST)
        if analysis_url.is_valid():
            #analysis_url_path = urlparse(analysis_url).path.split('/')
            #playlist_id = analysis_url_path[2]
            analysis_url.save()
        #
        # analysis_data = analysis_main.main(playlist_id)
        # svg = output_plot()
        # plt.cla()
        # return render(request, 'result.html', {'hist': hist}, svg)
        # response = redirect('/musicanalysis/result')
        return redirect('/musicanalysis/result')

    else:
        template_name = "index.html"
        form = PlaylistIdForm()
        context = {'form': form}
        return render(request, template_name, context)


def result(request):
    template_name = "result.html"
    return render(request, template_name)


def get_svg(request):

    csv_dir = settings.MEDIA_ROOT + "spotify_music_data.csv"

    def plot_histogram():
        df = pd.read_csv(csv_dir)
        print(df.describe())
        plt.switch_backend("AGG")
        plt.hist(df["popularity"], bins="auto")
        # plt.title('popularity histgram')
        plt.xlabel('popularity')
        plt.ylabel('frequency')

        plt.savefig(settings.MEDIA_ROOT + "hist.png")

    def convert_to_svg():
        buffer = io.BytesIO()  # バッファを作成
        plt.savefig(buffer, format='svg', bbox_inches='tight')  # バッファに一時保存
        s = buffer.getvalue()  # バッファの内容を s に渡す
        buffer.close()  # バッファはクローズ
        return s  # s を返す



    query = PlaylistIdModel.objects.order_by('id').last()
    analysis_url = query.playlist_id
    analysis_url_path = urlparse(analysis_url).path.split('/')
    playlist_id = analysis_url_path[2]
    analysis_data = analysis_main.main(playlist_id)

    # ヒストグラムを描画
    plot_histogram()
    svg = convert_to_svg()
    plt.cla()

    # csv保存ディレクトリを初期化
    # os.remove(csv_dir)

    response = HttpResponse(svg, content_type='image/svg+xml')
    return response
