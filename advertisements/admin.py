
from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['property', 'title', 'price']
    search_fields = ['property__name', 'title']
