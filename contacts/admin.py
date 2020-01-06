from django.contrib import admin
from .models import  Contacts

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'phone', 'email')
  list_display_links = ('id', 'name')
  list_filter = ('name','phone','email')
  list_editable = ('email',)
  search_fields = ('id', 'name', 'phone', 'email')
  list_per_page = 10

admin.site.register(Contacts, ContactsAdmin)