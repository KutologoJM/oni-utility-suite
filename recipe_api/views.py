from rest_framework.viewsets import *
from .models import *
from .serializers import *
from django.views.generic import *

# Create your views here.


class IngredientsViewSet(ModelViewSet):
    serializer_class = IngredientsSerializer
    queryset = IngredientsModel.objects.all()


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = RecipeModel.objects.all()


class SourcesViewSet(ModelViewSet):
    serializer_class = SourcesSerializer
    queryset = SourcesModel.objects.all()


class RecipeIngredientsViewSet(ModelViewSet):
    serializer_class = RecipeIngredientsSerializer
    queryset = RecipeIngredientsModel.objects.all()


class RecipeSourcesViewSet(ModelViewSet):
    serializer_class = RecipeSourcesSerializer
    queryset = RecipeSourcesModel.objects.all()


class IngredientSourcesViewSet(ModelViewSet):
    serializer_class = IngredientSourcesSerializer
    queryset = IngredientSourcesModel.objects.all()


class RecipeShowcaseView(ListView):
    model = RecipeModel
    template_name = "recipe_api/recipe_showcase.html"
    context_object_name = "recipes"
    queryset = RecipeModel.objects.all()
