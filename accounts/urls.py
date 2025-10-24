from django.urls import path, include
from .views import *

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("profile/", CustomProfileView.as_view(), name="profile"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path(
        "password_change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        CustomPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
