from django.db import models

# Create your models here.
class CityDestination(models.Model):
    city_name_destination = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name_destination