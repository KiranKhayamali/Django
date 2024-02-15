from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", {"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse("The current datetime is " + str(datetime.now()))

def about(request):
    return HttpResponse("Hi!, I am Kiran Khayamali,18 yearsold. Currently, Not involve in any employment sector.")

def electronics(request):
    items = ["Windows PC", "Apple Mac", "Apple Phone", "Lenovo", "Samsung", "Google", "Redmi", "OnePlus", "Vivo", "Oppo"]
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})
    elif request.method == 'POST':
        return HttpResponseNotFound("Page Not Found")
