from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls import reverse_lazy

from accounts import forms as custom_forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from . import serializers

User = get_user_model()

"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']

# Phase 2
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""


# Create your views here.
class CustomRegisterView(generic.CreateView):
    model = User
    form_class = custom_forms.CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class CustomLoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy("profile")
    redirect_field_name = "next"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/dashboard.html"


class CustomProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/profile.html"


class CustomLogoutView(auth_views.LogoutView):
    template_name = "accounts/logged_out.html"


class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = "accounts/password_change_form.html"
    success_url = reverse_lazy("profile")
    form_class = PasswordChangeForm
    extra_context = {"current_app": "accounts"}


class CustomPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"
    extra_context = {"current_app": "accounts"}


# ----------------------------------------------------
class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated]
