from django.db import models


class Vehicle(models.Model):
    price_usd = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Price, USD'
    )
    year_of_manufacture = models.IntegerField(verbose_name='Year Of Manufacture')
    mileage_km = models.IntegerField(verbose_name='Mileage, km')
    engine_capacity_liters = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name='Engine Capacity, liters'
    )
    num_seats = models.IntegerField(verbose_name='Seats In Vehicle')
    num_doors = models.IntegerField(verbose_name='Doors In Vehicle')
    description = models.TextField(
        blank=True,
        verbose_name='Vehicle Description'
    )
