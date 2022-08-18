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


class VehicleCategory(models.Model):
    title = models.CharField(max_length=20, verbose_name='Category')

    def __str__(self):
        return self.title


class VehicleFuel(models.Model):
    title = models.CharField(max_length=20, verbose_name='Fuel Type')

    def __str__(self):
        return self.title


class VehicleEngineCapacity(models.Model):
    engine_capacity_liters = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Engine Capacity (liters)'
    )

    def __str__(self):
        return self.engine_capacity_liters


class VehicleTransmission(models.Model):
    title = models.CharField(max_length=20, verbose_name='Transmission Type')

    def __str__(self):
        return self.title

