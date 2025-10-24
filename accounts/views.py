from django.contrib.auth.views import *
from .forms import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin


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
class CustomRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    next_page = reverse_lazy("profile")
    redirect_field_name = "next"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"


class CustomProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class CustomLogoutView(LogoutView):
    template_name = "accounts/logged_out.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change_form.html"
    success_url = reverse_lazy("profile")
    form_class = PasswordChangeForm
    extra_context = {"current_app": "accounts"}


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"
    extra_context = {"current_app": "accounts"}
