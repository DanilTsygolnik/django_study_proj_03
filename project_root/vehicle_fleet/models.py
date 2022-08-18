from django.db import models


class VehicleBrand(models.Model):
    title = models.CharField(max_length=20, verbose_name='Vehicle Brand')

    def __str__(self):
        return self.title


class VehicleModelInBrand(models.Model):
    vehicle_brand = models.ForeignKey(
        VehicleBrand,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=20, verbose_name='Vehicle Model')

    def __str__(self):
        return self.title

