from django.contrib import admin
from django.apps import apps
from accounts.models import CustomUser, CustomerProfile, ManagerProfile, AdminProfile
# Register your models here.


app = apps.get_app_config("accounts")

admin.site.register(CustomUser)
admin.site.register(CustomerProfile)
admin.site.register(ManagerProfile)
admin.site.register(AdminProfile)