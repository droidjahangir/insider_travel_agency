from django.contrib import admin
from .models import  Flights

# Register your models here.
class FlightsAdmin(admin.ModelAdmin):
  list_display = ('id', 'from_where', 'destination', 'airways', 'flight_time')
  list_display_links = ('id', 'airways')
  list_filter = ('destination',)
  list_editable = ('flight_time',)
  search_fields = ('id', 'from_where', 'destination', 'airways', 'flight_time')
  list_per_page = 10

admin.site.register(Flights, FlightsAdmin)

