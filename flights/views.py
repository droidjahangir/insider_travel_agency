from django.shortcuts import render, get_object_or_404
from .models import Flights
from airlines.models import Airlines
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import  city, adults, childs, rooms, airlines



# Create your views here.
def index(request):

    flights = Flights.objects.filter(is_published=True)
    airlines = Airlines.objects.filter(is_published=True)

    paginator = Paginator(flights, 10)
    page = request.GET.get('page')
    paged_flights = paginator.get_page(page)

    context = {
        'flights': paged_flights,
        'airlines': airlines
    }

    return render(request, 'flights/flights.html', context)


def flight(request, flight_id):
    flight = get_object_or_404(Flights, pk=flight_id)


    context = {
        'flight': flight
    }
    return render(request, 'flights/flight.html', context)


# def search(request):
#     queryset_list = Flights.objects.order_by('-list_date')
#     airlines = Airlines.objects.filter(is_published=True)

#     # where you want to go
#     if 'destination' in request.GET:
#         destination = request.GET['destination']
#         if destination:
#             queryset_list = queryset_list.filter(destination__iexact=destination)

#     # departure
#     if 'departure' in request.GET:
#         departure = request.GET['departure']
#         if departure:
#             queryset_list = queryset_list.filter(from_where__iexact=departure)

#     # destination
#     if 'destination' in request.GET:
#         destination = request.GET['destination']
#         if destination:
#             queryset_list = queryset_list.filter(destination__iexact=destination)

#     # adult
#     if 'adult' in request.GET:
#         adult = request.GET['adult']

#     # child
#     if 'child' in request.GET:
#         child = request.GET['child']

#     # rooms
#     if 'rooms' in request.GET:
#         rooms = request.GET['rooms']

#     context = {
#         'airlines': airlines,
#         'departure': departure,
#         'destination': destination,
#         'child': child,
#         'adult': adult,
#         'rooms': rooms,
#         'values': request.GET
#     }

#     return render(request, 'flights/search.html', context)
