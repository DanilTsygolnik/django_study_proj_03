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
        self.vehicle_id = kwargs['instance'].id
        super(VehicleAdminForm, self).__init__(*args,**kwargs)

    def clean(self):
        cleaned_data = super().clean()
        vehicle_owner_id_new = cleaned_data.get('owner').__dict__['id']
        vehicle_obj = Vehicle.objects.get(id=self.vehicle_id)
        vehicle_owner_id_old = vehicle_obj.__dict__['id']
        user_changed_owner = (vehicle_owner_id_old != vehicle_owner_id_new)
        vehicle_drivers = vehicle_obj.driver_set
        num_active_drivers = len(vehicle_drivers.filter(is_driving=True))
        vehicle_is_busy = (num_active_drivers != 0)
        import pdb; pdb.set_trace()
        if user_changed_owner and vehicle_is_busy:
            raise ValidationError(
                _("You cannot change the owner if the vehicle is busy.\n \
                  Change 'is_driving' field for the driver %(driver_id)s \
                  first."),
                code='changing_vehicle_owner_while_busy',
                params={'driver_id': 'driver_id_placeholder'},
            )
        return vehicle_owner_id_new
