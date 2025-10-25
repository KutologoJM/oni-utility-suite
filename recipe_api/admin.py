from django.apps import apps
from django.contrib import admin

# Register your models here.

app = apps.get_app_config("recipe_api")

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
