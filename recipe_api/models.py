from django.db.models import *
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth import get_user_model
from .utils import get_fallback_user, get_default_manager

User = get_user_model()

# Create your models here.


class IngredientsModel(Model):
    creator = ForeignKey(
        User,
        on_delete=SET(get_fallback_user),
        related_name="ingredient_owner",
        default=get_default_manager,
    )

    ingredient_name = CharField(max_length=50, unique=True)
    ingredient_wiki_url = URLField(max_length=100, blank=True)
    ingredient_image_url = URLField(max_length=100, blank=True)
    ingredient_description = TextField(null=True, max_length=200)

    food_quality = JSONField(help_text='{"Quality": "Standard", "Morale impact": "+2"}')

    spoil_time = PositiveIntegerField(blank=True, null=True)

    kcal_per_kg = PositiveIntegerField(blank=True, null=True)

    sources = ManyToManyField(
        "SourcesModel",
        through="IngredientSourcesModel",
        related_name="ingredient_sources",
    )

    slug = AutoSlugField(populate_from="ingredient_name", unique=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.ingredient_name


class RecipeModel(Model):
    creator = ForeignKey(
        User,
        on_delete=SET(get_fallback_user),
        related_name="recipe_owner",
        default=get_default_manager,
    )

    recipe_name = CharField(max_length=50, unique=True)
    recipe_wiki_url = URLField(max_length=100, blank=True)
    recipe_image_url = URLField(max_length=100, blank=True)
    recipe_description = TextField(null=True, max_length=200)

    dlc_name = CharField(max_length=50, null=True, blank=True)
    dlc_wiki_url = URLField(max_length=100, blank=True, null=True)
    dlc_image_url = URLField(max_length=100, blank=True, null=True)

    food_quality = JSONField(help_text='{"Quality": "Standard", "Morale impact": "+2"}')

    spoil_time = PositiveIntegerField(blank=True, null=True)

    kcal_per_kg = PositiveIntegerField(blank=True, null=True)

    ingredients = ManyToManyField(
        IngredientsModel,
        through="RecipeIngredientsModel",
        related_name="ingredients",
    )

    sources = ManyToManyField(
        "SourcesModel",
        through="RecipeSourcesModel",
        related_name="recipe_sources",
    )

    kcal_gained = CharField(max_length=50, null=True, blank=True)

    slug = AutoSlugField(populate_from="recipe_name", unique=True)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.recipe_name


class SourcesModel(Model):
    source_name = CharField(max_length=50, null=True, blank=True, unique=True)
    source_wiki_url = URLField(max_length=100, blank=True, null=True)
    source_image_url = URLField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Sources"

    def __str__(self):
        return self.source_name


class RecipeIngredientsModel(Model):
    creator = ForeignKey(
        User,
        on_delete=SET(get_fallback_user),
        related_name="recipe_ingredient_owner",
        default=get_default_manager,
    )
    ROLE_CHOICES = [("main", "Main"), ("alternate", "Alternate")]
    role = CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True)
    amount_required = CharField(max_length=50)

    recipe = ForeignKey(RecipeModel, on_delete=CASCADE)
    ingredient = ForeignKey(IngredientsModel, on_delete=CASCADE)

    class Meta:
        verbose_name = "Recipe Ingredient"
        verbose_name_plural = "Recipe Ingredients"

    def __str__(self):
        return f"{self.amount_required} of {self.ingredient.ingredient_name} for {self.recipe.recipe_name}"


class RecipeSourcesModel(Model):
    creator = ForeignKey(
        User,
        on_delete=SET(get_fallback_user),
        related_name="recipe_source_relationship_owner",
        default=get_default_manager,
    )
    recipe = ForeignKey(RecipeModel, on_delete=CASCADE)
    source = ForeignKey(SourcesModel, on_delete=CASCADE)

    class Meta:
        verbose_name = "Recipe Source"
        verbose_name_plural = "Recipe Sources"
        constraints = [
            UniqueConstraint(fields=["recipe", "source"], name="unique_recipe_source")
        ]

    def __str__(self):
        return f"{self.source.source_name} for {self.recipe.recipe_name}"


class IngredientSourcesModel(Model):
    creator = ForeignKey(
        User,
        on_delete=SET(get_fallback_user),
        related_name="ingredient_source_relationship_owner",
        default=get_default_manager,
    )
    ingredients = ForeignKey(IngredientsModel, on_delete=CASCADE)
    source = ForeignKey(SourcesModel, on_delete=CASCADE)

    class Meta:
        verbose_name = "Ingredient Source"
        verbose_name_plural = "Ingredient Sources"
        constraints = [
            UniqueConstraint(
                fields=["ingredients", "source"], name="unique_ingredient_source"
            )
        ]

    def __str__(self):
        return f"{self.source.source_name} for {self.ingredients.ingredient_name}"
