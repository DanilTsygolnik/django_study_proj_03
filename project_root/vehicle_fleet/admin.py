from django.contrib import admin
from .models import *


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'model_in_brand',
        'category',
        'year_of_manufacture',
        'mileage_km',
        'transmission',
        'fuel',
        'price_usd'
    )


admin.site.register(VehicleBrand)
admin.site.register(VehicleModelInBrand)
admin.site.register(VehicleCategory)
admin.site.register(VehicleFuel)
admin.site.register(VehicleEngineCapacity)
admin.site.register(VehicleTransmission)
admin.site.register(VehicleTypeOfDrive)
admin.site.register(VehicleNumSeats)
admin.site.register(VehicleNumDoors)
admin.site.register(VehicleBodyColor)
admin.site.register(Vehicle, VehicleAdmin)
