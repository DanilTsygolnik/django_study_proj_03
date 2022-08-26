from django.contrib import admin
from .models import *


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'model',
        'license_plate_num',
        'vehicle_type',
        'year_of_manufacture',
        'mileage_km',
        'price_usd',
    )
    list_display_links = ('id',)


admin.site.register(VehicleBrand)
admin.site.register(Vehicle, VehicleAdmin)
