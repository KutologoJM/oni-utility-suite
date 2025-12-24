from django.contrib import admin
from .models import IngredientsModel, RecipesModel, SourcesModel, RecipeSourcesModel, RecipeIngredientsModel, IngredientSourcesModel

# Register your models here.

admin.site.register(IngredientsModel)
admin.site.register(RecipesModel)
admin.site.register(SourcesModel)
admin.site.register(RecipeIngredientsModel)
admin.site.register(RecipeSourcesModel)
admin.site.register(IngredientSourcesModel)
