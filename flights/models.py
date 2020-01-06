from django.db import models
from datetime import datetime
from city.models import City
from city_destination.models import CityDestination
from airlines.models import Airlines



# Create your models here.

class Flights(models.Model):
    from_where = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    destination = models.ForeignKey(CityDestination, on_delete=models.DO_NOTHING)
    airways = models.ForeignKey(Airlines, on_delete=models.DO_NOTHING)
    flight_time = models.DateTimeField(blank=True)
    price = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)





