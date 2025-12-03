from rest_framework import serializers
from recipe_api import models


class SourcesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SourcesModel
        fields = [
            "source_name",
            "source_wiki_url",
            "source_image_url",
        ]


class IngredientSourcesSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)
    ingredient = serializers.CharField(
        source="ingredients.ingredient_name", read_only=True
    )
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=models.IngredientsModel.objects.all(),  # noqa
        source="ingredients",
        write_only=True,
    )
    ingredient_source = serializers.CharField(
        source="source.source_name", read_only=True
    )
    ingredient_source_id = serializers.PrimaryKeyRelatedField(
        queryset=models.SourcesModel.objects.all(), source="source", write_only=True  # noqa
    )

    class Meta:
        model = models.IngredientSourcesModel
        fields = [
            "creator",
            "ingredient",
            "ingredient_id",
            "ingredient_source",
            "ingredient_source_id",
        ]


class IngredientsSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)
    sources = SourcesSerializer(many=True, read_only=True)

    class Meta:
        model = models.IngredientsModel
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


class RecipeIngredientsSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(read_only=True, many=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=models.IngredientsModel.objects.all(),  # noqa
        source="ingredient",
        write_only=True,
    )
    recipe = serializers.CharField(source="recipe.recipe_name", read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=models.RecipeModel.objects.all(), source="recipe", write_only=True  # noqa
    )
    creator = serializers.CharField(source="creator.username", read_only=True)

    class Meta:
        model = models.RecipeIngredientsModel
        fields = [
            "recipe",
            "recipe_id",
            "ingredients",
            "ingredient_id",
            "creator",
            "role",
            "amount_required",
        ]


class RecipeSourcesSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.username", read_only=True)
    recipe = serializers.CharField(source="recipe.recipe_name", read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=models.RecipeModel.objects.all(),  # noqa
        source="recipe",
        write_only=True,
    )
    recipe_source = serializers.CharField(source="source.source_name", read_only=True)
    recipe_source_id = serializers.PrimaryKeyRelatedField(
        queryset=models.SourcesModel.objects.all(), source="source", write_only=True  # noqa
    )

    class Meta:
        model = models.RecipeSourcesModel
        fields = ["creator", "recipe", "recipe_id", "recipe_source", "recipe_source_id"]
        ordering = ["recipe_source", "recipe_source_id"]


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientsSerializer(
        source="recipeingredientsmodel_set", read_only=True, many=True  # noqa
    )
    sources = RecipeSourcesSerializer(
        source="recipesourcesmodel_set", read_only=True, many=True  # noqa
    )
    creator = serializers.CharField(source="creator.username", read_only=True)

    class Meta:
        model = models.RecipeModel
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
