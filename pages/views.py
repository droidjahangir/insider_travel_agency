from django.shortcuts import render, get_object_or_404
from flights.choices import  adults, childs, rooms, city
from airlines.models import Airlines
from flights.models import Flights
from city.models import City
from city_destination.models import CityDestination


# Create your views here.


def index(request):

    airways = get_object_or_404(Airlines, pk=11)    
    airways2 = get_object_or_404(Airlines, pk=12)  

    context = {
        'city': city,
        'adults': adults,
        'childs': childs,
        'rooms': rooms,
        'airways': airways,
        'airways2': airways2
    }

    return render(request, 'pages/index.html', context)

def about(request):

    return render(request, 'pages/about.html')


def search(request):
    queryset_list = Flights.objects.order_by('-flight_date')
    airlines = Airlines.objects.filter(is_published=True)

    # where you want to go
    if 'destination' in request.GET:
        destination = request.GET['destination']
        destination_object = get_object_or_404(CityDestination, city_name_destination=destination)  
        if destination_object:
            queryset_list = queryset_list.filter(destination_id=destination_object.id)

    # departure
    if 'departure' in request.GET:
        departure = request.GET['departure']
        departure_object = get_object_or_404(City, city_name=departure)
        if departure_object:
            queryset_list = queryset_list.filter(from_where_id=departure_object.id)

    # destination
    if 'destination' in request.GET:
        destination = request.GET['destination']
        destination_object = get_object_or_404(CityDestination, city_name_destination=destination)  
        if destination_object:
            queryset_list = queryset_list.filter(destination_id=destination_object.id)

    # # adult
    # if 'adult' in request.GET:
    #     adults = request.GET['adult']

    # # child
    # if 'child' in request.GET:
    #     childs = request.GET['child']

    # # rooms
    # if 'rooms' in request.GET:
    #     rooms = request.GET['rooms']

    context = {
        'flights': queryset_list,
        'values': request.GET
    }

    return render(request, 'pages/search.html', context)