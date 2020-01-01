from django.shortcuts import render
from flights.choices import  adults, childs, rooms, airports, countrys


# Create your views here.


def index(request):

    context = {
    'countries': countrys,
    'airports': airports,
    'adults': adults,
    'childs': childs,
    'rooms': rooms,
    }

    return render(request, 'pages/index.html', context)

def about(request):

    return render(request, 'pages/about.html')