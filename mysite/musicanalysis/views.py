from django.shortcuts import render

# Create your views here.
def top(request):
    return render(request, 'index.html')