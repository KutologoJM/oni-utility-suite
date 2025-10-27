from rest_framework.serializers import *

from accounts import serializers
from .models import *


class SourcesSerializer(ModelSerializer):

    class Meta:
        model = SourcesModel
        fields = [
            "source_name",
            "source_wiki_url",
            "source_image_url",
        ]


class IngredientSourcesSerializer(ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)
    ingredient = serializers.CharField(
        source="ingredients.ingredient_name", read_only=True
    )
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=IngredientsModel.objects.all(),  # noqa
        source="ingredients",
        write_only=True,
    )
    ingredient_source = serializers.CharField(
        source="source.source_name", read_only=True
    )
    ingredient_source_id = serializers.PrimaryKeyRelatedField(
        queryset=SourcesModel.objects.all(), source="source", write_only=True  # noqa
    )

    class Meta:
        model = IngredientSourcesModel
        fields = [
            "creator",
            "ingredient",
            "ingredient_id",
            "ingredient_source",
            "ingredient_source_id",
        ]


class IngredientsSerializer(ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)
    sources = SourcesSerializer(many=True, read_only=True)

    class Meta:
        model = IngredientsModel
        fields = [
            "creator",
            "ingredient_name",
            "ingredient_wiki_url",
            "ingredient_image_url",
            "ingredient_description",
            "food_quality",
            "spoil_time",
            "kcal_per_kg",
            "sources",
            "slug",
        ]


class RecipeIngredientsSerializer(ModelSerializer):
    ingredients = IngredientsSerializer(read_only=True, many=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=IngredientsModel.objects.all(),  # noqa
        source="ingredient",
        write_only=True,
    )
    recipe = serializers.CharField(source="recipe.recipe_name", read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=RecipeModel.objects.all(), source="recipe", write_only=True  # noqa
    )
    creator = serializers.CharField(source="creator.username", read_only=True)

    class Meta:
        model = RecipeIngredientsModel
        fields = [
            "recipe",
            "recipe_id",
            "ingredients",
            "ingredient_id",
            "creator",
            "role",
            "amount_required",
        ]


class RecipeSourcesSerializer(ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)
    recipe = serializers.CharField(source="recipe.recipe_name", read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=RecipeModel.objects.all(),  # noqa
        source="recipe",
        write_only=True,
    )
    recipe_source = serializers.CharField(source="source.source_name", read_only=True)
    recipe_source_id = serializers.PrimaryKeyRelatedField(
        queryset=SourcesModel.objects.all(), source="source", write_only=True  # noqa
    )

    class Meta:
        model = RecipeSourcesModel
        fields = ["creator", "recipe", "recipe_id", "recipe_source", "recipe_source_id"]
        ordering = ["recipe_source", "recipe_source_id"]


class RecipeSerializer(ModelSerializer):
    ingredients = RecipeIngredientsSerializer(
        source="recipeingredientsmodel_set", read_only=True, many=True  # noqa
    )
    sources = RecipeSourcesSerializer(
        source="recipesourcesmodel_set", read_only=True, many=True  # noqa
    )
    creator = serializers.CharField(source="creator.username", read_only=True)

    class Meta:
        model = RecipeModel
        fields = [
            "creator",
            "recipe_name",
            "recipe_wiki_url",
            "recipe_image_url",
            "recipe_description",
            "dlc_name",
            "dlc_wiki_url",
            "dlc_image_url",
            "food_quality",
            "spoil_time",
            "kcal_per_kg",
            "ingredients",
            "sources",
            "kcal_gained",
            "slug",
        ]
