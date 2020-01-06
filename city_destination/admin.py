from django.contrib import admin
from .models import  CityDestination

# Register your models here.

class CityDestinationAdmin(admin.ModelAdmin):
  list_display = ('id', 'city_name_destination')
  list_display_links = ('id', 'city_name_destination')
  list_filter = ('city_name_destination',)
  search_fields = ('id', 'city_name_destination')
  list_per_page = 10

admin.site.register(CityDestination, CityDestinationAdmin)