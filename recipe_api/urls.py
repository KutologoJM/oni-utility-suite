from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

from .views import workshop_template_view

internal_router = DefaultRouter()
internal_router.register("ingredients", views.IngredientsViewSet)
internal_router.register("recipe", views.RecipeViewSet)
internal_router.register("sources", views.SourcesViewSet)
internal_router.register("recipe-ingredients", views.RecipeIngredientsViewSet)
internal_router.register("recipe-sources", views.RecipeSourcesViewSet)
internal_router.register("ingredient-sources", views.IngredientSourcesViewSet)

public_router = DefaultRouter()

urlpatterns = [
    path("", workshop_template_view, name="workshop_template"),
    path("public/", include(public_router.urls)),
    path("internal/", include(internal_router.urls)),
    path("showcase/", views.RecipeShowcaseView.as_view()),
    path("showcase/<slug:slug>/", views.RecipeDetailedView.as_view()),
    path("experimental/<slug:slug>/", views.Experimental.as_view()),

]

