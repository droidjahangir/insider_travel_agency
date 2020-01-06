from django.contrib import admin
from .models import  Airlines


# Register your models here.
class AirlinesAdmin(admin.ModelAdmin):
  list_display = ('id', 'airways_name', 'airways_flight_code')
  list_display_links = ('id', 'airways_name')
  list_filter = ('airways_flight_code',)
  list_editable = ('airways_flight_code',)
  search_fields = ('id', 'airways_name', 'airways_flight_code')
  list_per_page = 10

admin.site.register(Airlines, AirlinesAdmin)