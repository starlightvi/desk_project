from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display= ('id', 'title', 'is_published', 'price', 'city', 'realtor', )
    list_display_links=('id', 'title')
    list_filter=('id', 'realtor', 'city')
    list_editable=('is_published',)
    search_fields=('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page=25
admin.site.register(Listing, ListingAdmin)
# Register your models here.

