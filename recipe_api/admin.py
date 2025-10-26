from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(IngredientsModel)
admin.site.register(RecipeModel)
admin.site.register(SourcesModel)
admin.site.register(RecipeIngredientsModel)
admin.site.register(RecipeSourcesModel)
admin.site.register(IngredientSourcesModel)
