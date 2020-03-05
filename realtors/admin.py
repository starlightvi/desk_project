from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id', 'name','email', 'hire_date')
    list_display_link=('id', 'name')
    search_fields=('name',)
    list_per_page=25
    list_filter=('id', 'name')
# Register your models here.
admin.site.register(Realtor, RealtorAdmin)