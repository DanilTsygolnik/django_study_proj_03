from django.db import models


class Driver(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last Name'
    )
    num_years_experience = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Years Of Experience'
    )
    employer = models.ForeignKey(
        'Enterprise', 
        blank=True,
        null = True,
        on_delete=models.SET_NULL
    )
    is_driving = models.BooleanField(verbose_name='Is Driving')
    assigned_vehicles = models.ManyToManyField(
        'Vehicle',
        blank=True,
    )


class Enterprise(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Company Name'
    )

    def __str__(self):
        return self.title


class VehicleBrand(models.Model):
    title = models.CharField(max_length=20, verbose_name='Vehicle Brand')

    def __str__(self):
        return self.title


class Vehicle(models.Model):
    brand = models.ForeignKey(
        VehicleBrand, 
        on_delete=models.CASCADE
    )
    model = models.CharField(
        max_length=20,
        verbose_name='Vehicle Model'
    )
    license_plate_num = models.CharField(
        max_length=10,
        verbose_name='License Plate Number'
    )
    vehicle_type = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        verbose_name='Vehicle Type'
    )
    year_of_manufacture = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Year Of Manufacture'
    )
    mileage_km = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Mileage, km'
    )
    price_usd = models.DecimalField(
        blank=True,
        null=True,
        max_digits=11,
        decimal_places=2,
        verbose_name='Price, USD'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Vehicle Description'
    )
    owner = models.ForeignKey(
        Enterprise, 
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )

