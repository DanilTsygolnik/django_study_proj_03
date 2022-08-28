from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Vehicle, Driver


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
        try:
            active_driver = self.vehicle.driver_set.get(is_driving=True)
            vehicle_is_busy = True
        except Driver.DoesNotExist:
            vehicle_is_busy = False
        if user_changed_owner and vehicle_is_busy:
            self.data = self.data.copy()
            self.data['owner'] = vehicle_owner_old
            raise ValidationError(
                _("If you want to change the owner, unset active driver first. \
                    Currently active driver: %(driver)s"
                ),
                code='changing_vehicle_owner_while_busy',
                params={'driver': active_driver},
            )
