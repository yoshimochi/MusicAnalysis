from django.shortcuts import render

from .forms import SearchPassForm


# Create your views here.
def top(request):
    if request.method == "POST":
        search_pass = request.POST["search_pass"]
        form = SearchPassForm(initial={'search_pass': search_pass})
    else:
        return render(request, 'index.html')
