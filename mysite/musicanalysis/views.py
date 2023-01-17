import urllib.parse

from django.shortcuts import render

from .forms import SearchPassForm


# Create your views here.
def top(request):
    if request.method == "POST":
        analysis_url = request.POST['url']
        analysis_url_path = urllib.parse.urlparse(analysis_url).path.split('/')
        playlist_id = analysis_url_path[2]

        return render(request, 'result.html')

    else:
        template_name = "index.html"
        form = SearchPassForm()
        context = {'form': form}
        return render(request, template_name, context)
