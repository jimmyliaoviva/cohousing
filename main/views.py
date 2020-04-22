from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def redirect(request):
    return render(request, 'redirectPage.html')


def search(request):
    return render(request, 'search.html')
