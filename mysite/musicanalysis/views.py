import os
import shutil
from urllib.parse import urlparse
import matplotlib

from mysite import settings

from django.shortcuts import render, redirect

from .forms import PlaylistIdForm
from .autio_features import main
from .models import PlaylistIdModel
from .graph import plot_histogram, plot_heatmap


# Create your views here.
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
    graph_pass = 'static/png'
    dir = os.path.join(BASE_DIR, graph_pass)
    file_lists = os.listdir(dir)

    # 画像保存用ディレクトリを初期化
    if len(file_lists) > 0:
        for file_list in file_lists:
            os.remove(dir + "/" + file_list)


    print(BASE_DIR)
    query = PlaylistIdModel.objects.order_by("id").last()
    analysis_url = query.playlist_id
    analysis_url_path = urlparse(analysis_url).path.split("/")
    playlist_id = analysis_url_path[2]
    # main(playlist_id)
    plot_histogram()
    plot_heatmap()
    template_name = "result.html"
    return render(request, template_name)
