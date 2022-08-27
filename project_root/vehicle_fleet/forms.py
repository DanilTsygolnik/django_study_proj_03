from django import forms

from .models import Vehicle


class VehicleAdminForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def clean_owner_id(self):
        field_id = 'owner_id'
        value_form_cleaned = self.cleaned_data[field_id]
        vehicle_id = self.cleaned_data['id']
        value_database = Vehicle.objects.get(id=vehicle_id).__dict__[field_id]
        user_changed_field = (value_form_cleaned != value_database)
        num_vehicle_active_drivers = len(self.driver_set.filter(is_driving=True))
        vehicle_is_busy = (num_vehicle_active_drivers != 0)
        if user_changed_field and vehicle_is_busy:
            raise ValidationError(
                _("You cannot change the owner if the vehicle is busy.\n \
                  Change 'is_driving' field for the driver %(driver_id)s \
                  first."),
                code='changing_vehicle_owner_while_busy',
                params={'driver_id': 'driver_id_placeholder'},
            )
        return value_form_cleaned

