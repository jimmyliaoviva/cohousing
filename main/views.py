from django.shortcuts import render
from main.models import house, houseHolder


# Create your views here.
def index(request):
    return render(request, 'index.html')


def redirect(request):
    return render(request, 'redirectPage.html')


def search(request):
    houses = house.objects.all()
    return render(request, 'search.html', locals())


def houseDetail(request, id):
    item = house.objects.get(id=id)
    holder = houseHolder.objects.get(id=id)
    return render(request, 'houseDetail.html', locals())


def dashboard(request):
    return render(request, 'dashboard.html')


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')
