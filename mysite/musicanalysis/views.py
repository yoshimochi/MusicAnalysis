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
from .autio_features import main
from .models import PlaylistIdModel
from .graph import plot_histogram, convert_to_svg1, convert_to_svg2, plt_heatmap


# Create your views here.
def top(request):
    if request.method == "POST":

        analysis_url = PlaylistIdForm(request.POST)
        if analysis_url.is_valid():
            analysis_url.save()

        response = redirect('/musicanalysis/result')
        return response

    else:
        template_name = "index.html"
        form = PlaylistIdForm()
        context = {'form': form}
        return render(request, template_name, context)


def result(request):
    query = PlaylistIdModel.objects.order_by('id').last()
    analysis_url = query.playlist_id
    analysis_url_path = urlparse(analysis_url).path.split('/')
    playlist_id = analysis_url_path[2]
    # main(playlist_id)
    plot_histogram()
    plt_heatmap()
    template_name = "result.html"
    return render(request, template_name)


def get_svg(request):
    plot_histogram()
    #svg1 = convert_to_svg1()

    response = HttpResponse(svg1, content_type='image/svg+xml')
    return response


def get_heat(request):
    plt_heatmap()
    #svg2 = convert_to_svg2()

    response = HttpResponse(svg2, content_type='image/svg+xml')
    return response
