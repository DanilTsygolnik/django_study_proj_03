from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Vehicle


class VehicleAdminForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
        }

    def __init__(self, *args, **kwargs):
        self.vehicle = kwargs['instance']
        super(VehicleAdminForm, self).__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super().clean()
        vehicle_owner_new = cleaned_data.get('owner')
        vehicle_owner_old = self.vehicle.owner
        user_changed_owner = (vehicle_owner_new.id != vehicle_owner_old.id)
        vehicle_drivers = self.vehicle.driver_set
        num_active_drivers = len(vehicle_drivers.filter(is_driving=True))
        vehicle_is_busy = (num_active_drivers != 0)
        if user_changed_owner and vehicle_is_busy:
            self.data = self.data.copy()
            self.data['owner'] = vehicle_owner_old
            raise ValidationError(
                _("You cannot change the owner if the vehicle is busy.\n \
                  Change 'is_driving' field for the driver %(driver_id)s \
                  first."),
                code='changing_vehicle_owner_while_busy',
                params={'driver_id': 'driver_id_placeholder'},
            )
