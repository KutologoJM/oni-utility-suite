from rest_framework.serializers import *
from .models import *


class IngredientsSerializer(ModelSerializer):

    class Meta:
        model = IngredientsModel
        fields = "__all__"


class RecipeSerializer(ModelSerializer):

    class Meta:
        model = RecipeModel
        fields = "__all__"


class SourcesSerializer(ModelSerializer):

    class Meta:
        model = SourcesModel
        fields = "__all__"


class RecipeIngredientsSerializer(ModelSerializer):

    class Meta:
        model = RecipeIngredientsModel
        fields = "__all__"


class RecipeSourcesSerializer(ModelSerializer):

    class Meta:
        model = RecipeSourcesModel
        fields = "__all__"


class IngredientSourcesSerializer(ModelSerializer):

    class Meta:
        model = IngredientSourcesModel
        fields = "__all__"
