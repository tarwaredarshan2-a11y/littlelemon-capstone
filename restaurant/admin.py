from django.contrib import admin
from .models import MenuItem, Booking


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    search_fields = ('title',)
    list_filter = ('price',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date', 'booking_time', 'table_number', 'booking_reference')
    search_fields = ('name', 'booking_reference')
    list_filter = ('booking_date', 'no_of_guests')
