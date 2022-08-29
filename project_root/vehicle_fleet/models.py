from django.db import models
from django.contrib.auth.models import AbstractUser


class Manager(AbstractUser):
    pass # For now we do nothinng

    def __str__(self):
        return self.username
