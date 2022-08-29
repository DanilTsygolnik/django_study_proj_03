from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import VehicleAdminForm


class ManagerAdmin(UserAdmin):
    model = Manager
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )


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


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Enterprise)
admin.site.register(VehicleBrand)
admin.site.register(Vehicle, VehicleAdmin)
