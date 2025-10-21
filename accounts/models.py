from django.contrib.auth.models import AbstractUser
from django.db.models import *


# Create your models here.


class CustomUser(AbstractUser):
    class Role(TextChoices):
        CUSTOMER = 'CUSTOMER', 'Customer'
        MANAGER = 'MANAGER', 'Manager'
        ADMIN = 'ADMIN', 'Admin'

    role = CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    @property
    def is_customer(self):
        return self.role == self.Role.CUSTOMER

    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    def __str__(self):
        return f"{self.username} ({self.role})"


class BaseProfile(Model):
    user = OneToOneField(CustomUser, on_delete=CASCADE)

    class Meta:
        abstract = True


class CustomerProfile(BaseProfile):
    pass


class ManagerProfile(BaseProfile):
    pass


class AdminProfile(BaseProfile):
    pass
