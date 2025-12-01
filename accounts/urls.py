from django.urls import path, include
from rest_framework import routers
from accounts import views


router = routers.DefaultRouter()
router.register("groups", views.GroupViewSet)
router.register("users", views.UserViewSet)

urlpatterns = [
    path("user-management/", include(router.urls)),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("profile/", views.CustomProfileView.as_view(), name="profile"),
    path("register/", views.CustomRegisterView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.CustomPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
