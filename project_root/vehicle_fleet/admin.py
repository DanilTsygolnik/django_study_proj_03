from django.contrib import admin
from .models import *
from .forms import VehicleAdminForm

class DriverAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'first_name',
    'last_name',
    'num_years_experience',
    'employer',
    'is_driving'
    )


class VehicleAdmin(admin.ModelAdmin):
    form = VehicleAdminForm
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


admin.site.register(Driver, DriverAdmin)
admin.site.register(Enterprise)
admin.site.register(VehicleBrand)
admin.site.register(Vehicle, VehicleAdmin)
