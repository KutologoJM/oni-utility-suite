from django.contrib.auth.models import AbstractUser, Group
from django.db.models import *


# Create your models here.


class CustomUser(AbstractUser):

    @property
    def is_customer(self):
        return self.groups.filter(name='Customer').exists()

    @property
    def is_manager(self):
        return self.groups.filter(name='Manager').exists()

    @property
    def is_admin(self):
        return self.groups.filter(name='Admin').exists()

    def __str__(self):
        primary_group = self.groups.first()
        return f"{self.username} ({primary_group.name if primary_group else 'No Group'})"


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
