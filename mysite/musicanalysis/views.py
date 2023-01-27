import os
from urllib.parse import urlparse

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PlaylistIdForm
from .autio_features import output_csv
from .models import PlaylistUrlModel
from .graph import plot_histogram, plot_heatmap
from mysite import settings


def top(request):
    if request.method == "POST":
        analysis_url = PlaylistIdForm(request.POST)
        if analysis_url.is_valid():
            analysis_url.save()

        response = redirect("/musicanalysis/analysis/result")
        return response

    else:
        template_name = "index.html"
        form = PlaylistIdForm()
        context = {"form": form}
        return render(request, template_name, context)


def result(request):
    template_name = "analysis/result.html"
    graph_pass = 'static/png'
    save_dir = os.path.join(settings.BASE_DIR, graph_pass)
    file_lists = os.listdir(save_dir)

    # 画像保存用ディレクトリを初期化
    if len(file_lists) > 0:
        for file_list in file_lists:
            os.remove(save_dir + "/" + file_list)

    # 登録したIDの中で最新のレコードを取得する
    query = PlaylistUrlModel.objects.order_by("id").last()
    analysis_url = query.playlist_url
    analysis_url_path = urlparse(analysis_url).path.split("/")

    # URLの中からプレイリストIDを取得
    playlist_id = analysis_url_path[2]

    # 分析用データを保存
    output_csv(playlist_id)

    csv_path = settings.MEDIA_ROOT + "spotify_music_data.csv"
    if os.path.exists(csv_path):
        # histgramを描画して保存
        plot_histogram()
        # ヒートマップ描画して保存
        plot_heatmap()
    else:
        messages.error(request, "グラフ描画用のcsvが見つかりません")

    return render(request, template_name)

# @require_http_methods(["GET", "POST"])
# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(...)
#         else:
#             form = UserCreationForm()
#         return render(request, "signup.html", {'form': form})
