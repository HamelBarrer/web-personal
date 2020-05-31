from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=14)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
