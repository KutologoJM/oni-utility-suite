from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from django.views.generic import ListView, DetailView

# Create your views here.


class IngredientsViewSet(ModelViewSet):
    serializer_class = serializers.IngredientsSerializer
    queryset = models.IngredientsModel.objects.all()
    lookup_field = "slug"


class RecipeViewSet(ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = models.RecipeModel.objects.all()
    lookup_field = "slug"


class SourcesViewSet(ModelViewSet):
    serializer_class = serializers.SourcesSerializer
    queryset = models.SourcesModel.objects.all()


class RecipeIngredientsViewSet(ModelViewSet):
    serializer_class = serializers.RecipeIngredientsSerializer
    queryset = models.RecipeIngredientsModel.objects.all()


class RecipeSourcesViewSet(ModelViewSet):
    serializer_class = serializers.RecipeSourcesSerializer
    queryset = models.RecipeSourcesModel.objects.all()


class IngredientSourcesViewSet(ModelViewSet):
    serializer_class = serializers.IngredientSourcesSerializer
    queryset = models.IngredientSourcesModel.objects.all()


class RecipeShowcaseView(ListView):
    model = models.RecipeModel
    template_name = "recipe_api/recipe_showcase.html"
    context_object_name = "recipes"
    queryset = models.RecipeModel.objects.all()


class RecipeDetailedView(DetailView):
    model = models.RecipeModel
    template_name = "recipe_api/detailed_recipe.html"
    context_object_name = "recipe"
    queryset = models.RecipeModel.objects.all()
    lookup_field = "slug"
    slug_url_kwarg = "slug"


class Experimental(DetailView):
    model = models.RecipeModel
    template_name = "recipe_api/experimental.html"
    context_object_name = "recipe"
    queryset = models.RecipeModel.objects.all()
    lookup_field = "slug"
    slug_url_kwarg = "slug"
