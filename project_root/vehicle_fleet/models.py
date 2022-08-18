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


class VehicleTypeOfDrive(models.Model):
    title = models.CharField(max_length=20, verbose_name='Type Of Drive')

    def __str__(self):
        return self.title


class VehicleNumSeats(models.Model):
    num_seats = models.IntegerField(verbose_name='Number Of Seats')

    def __str__(self):
        return self.num_seats


class VehicleNumDoors(models.Model):
    num_doors = models.IntegerField(verbose_name='Number Of Doors')

    def __str__(self):
        return self.num_doors


class VehicleBodyColor(models.Model):
    title = models.CharField(max_length=20, verbose_name='Vehicle Body Color')

    def __str__(self):
        return self.title


class Vehicle(models.Model):
    brand = models.ForeignKey(
        VehicleBrand, 
        on_delete=models.CASCADE
    )
    model_in_brand = models.ForeignKey(
        VehicleModelInBrand, 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        VehicleCategory, 
        on_delete=models.PROTECT
    )
    price_usd = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        verbose_name='Price, USD'
    )
    year_of_manufacture = models.IntegerField(verbose_name='Year Of Manufacture')
    mileage_km = models.IntegerField(verbose_name='Mileage, km')
    fuel = models.ForeignKey(
        VehicleFuel, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    engine_capacity = models.ForeignKey(
        VehicleEngineCapacity, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    transmission = models.ForeignKey(
        VehicleTransmission, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    type_of_drive = models.ForeignKey(
        VehicleTypeOfDrive, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    num_seats = models.ForeignKey(
        VehicleNumSeats, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    num_doors = models.ForeignKey(
        VehicleNumDoors, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    body_color = models.ForeignKey(
        VehicleBodyColor, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Vehicle Description'
    )

    def __str__(self):
        return self.model_in_brand.title

