from django.contrib import admin
from .models import *


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
admin.site.register(Vehicle)
