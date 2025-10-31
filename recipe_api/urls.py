from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

internal_router = DefaultRouter()
internal_router.register("ingredients", IngredientsViewSet)
internal_router.register("recipe", RecipeViewSet)
internal_router.register("sources", SourcesViewSet)
internal_router.register("recipe-ingredients", RecipeIngredientsViewSet)
internal_router.register("recipe-sources", RecipeSourcesViewSet)
internal_router.register("ingredient-sources", IngredientSourcesViewSet)

public_router = DefaultRouter()

urlpatterns = [
    path("", include(public_router.urls)),
    path("internal/", include(internal_router.urls)),
    path("showcase/", RecipeShowcaseView.as_view()),
    path("showcase/<slug:slug>/", RecipeDetailedView.as_view()),
    path("experimental/<slug:slug>/", Experimental.as_view()),

]
