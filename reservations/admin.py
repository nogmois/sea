
from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['property', 'start_date', 'end_date']
    search_fields = ['property__name', 'start_date', 'end_date']