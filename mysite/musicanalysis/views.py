import urllib.parse
import matplotlib
#バックエンドを指定
import matplotlib.pyplot as plt

matplotlib.use('Agg')
import matplotlib.pyplot as pl

from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchPassForm
from . import analysis_main


# Create your views here.
def top(request):
    if request.method == "POST":
        analysis_url = request.POST['url']
        analysis_url_path = urllib.parse.urlparse(analysis_url).path.split('/')
        playlist_id = analysis_url_path[2]

        hist = analysis_main.main(playlist_id)

        return render(request, 'result.html', {'hist': hist})

    else:
        template_name = "index.html"
        form = SearchPassForm()
        context = {'form': form}
        return render(request, template_name, context)

