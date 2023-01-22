import os
from urllib.parse import urlparse
from django.shortcuts import render, redirect

from .forms import PlaylistIdForm
from .autio_features import output_csv
from .models import PlaylistUrlModel
from .graph import plot_histogram, plot_heatmap
from mysite.settings import BASE_DIR


def top(request):
    if request.method == "POST":
        analysis_url = PlaylistIdForm(request.POST)
        if analysis_url.is_valid():
            analysis_url.save()

        response = redirect("/musicanalysis/result")
        return response

    else:
        template_name = "index.html"
        form = PlaylistIdForm()
        context = {"form": form}
        return render(request, template_name, context)


def result(request):
    template_name = "result.html"
    graph_pass = 'static/png'
    save_dir = os.path.join(BASE_DIR, graph_pass)
    file_lists = os.listdir(save_dir)

    # 画像保存用ディレクトリを初期化
    if len(file_lists) > 0:
        for file_list in file_lists:
            os.remove(dir + "/" + file_list)

    # 登録したIDの中で最新のレコードを取得する
    query = PlaylistUrlModel.objects.order_by("id").last()
    check_url = "https://open.spotify.com/playlist/"
    analysis_url = query.playlist_url
    analysis_url_path = urlparse(analysis_url).path.split("/")

    # URLの中からプレイリストIDを取得
    playlist_id = analysis_url_path[2]

    # 分析用データを保存
    try:
        output_csv(playlist_id)
    except Exception as e:
        error_message = "csvファイルの作成に失敗しました。"
        return render(request, template_name, error_message)

    # histgramを描画して保存
    plot_histogram()
    # ヒートマップ描画して保存
    plot_heatmap()


    return render(request, template_name)
