from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='flights'),
    # /listings/23
    path('<int:flight_id>', views.flight, name='flight'),
    # path('search', views.search, name='search'),
]
