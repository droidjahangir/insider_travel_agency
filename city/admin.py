from django.contrib import admin
from .models import  City

# Register your models here.

class CityAdmin(admin.ModelAdmin):
  list_display = ('id', 'city_name')
  list_display_links = ('id', 'city_name')
  list_filter = ('city_name',)
  search_fields = ('id', 'city_name')
  list_per_page = 10

admin.site.register(City, CityAdmin)
