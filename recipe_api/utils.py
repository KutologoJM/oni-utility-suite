from django.contrib.auth import get_user_model


User = get_user_model()


def get_fallback_user():
    # Try to get an existing fallback user
    fallback = User.objects.get(username="manager_Abe")
    return fallback


def get_default_manager():
    default = User.objects.get(username="manager_Abe")
    return default
