from django import forms
from django.core.exceptions import ValidationError

from .models import Vehicle


class VehicleAdminForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.vehicle_id = kwargs['id']
        super(VehicleAdminForm, self).__init__(self, *args,**kwargs)

    def clean(self):
        cleaned_data = super().clean()
        owner_field_id = 'owner_id'
        vehicle_owner_id_new = cleaned_data.get(owner_field_id)
        vehicle_id = cleaned_data.get('id')
        vehicle_obj = Vehicle.objects.get(id=vehicle_id)
        vehicle_owner_id_old = vehicle_obj.__dict__[owner_field_id]
        user_changed_owner = (vehicle_owner_id_old != vehicle_owner_id_new)
        vehicle_drivers = vehicle_obj.driver_set
        num_active_drivers = len(vehicle_drivers.filter(is_driving=True))
        vehicle_is_busy = (num_active_drivers != 0)
        if user_changed_owner and vehicle_is_busy:
            raise ValidationError(
                _("You cannot change the owner if the vehicle is busy.\n \
                  Change 'is_driving' field for the driver %(driver_id)s \
                  first."),
                code='changing_vehicle_owner_while_busy',
                params={'driver_id': 'driver_id_placeholder'},
            )
        return vehicle_owner_id_new
