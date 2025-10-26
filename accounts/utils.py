from django.contrib.auth import get_user_model
from accounts.models import *


User = get_user_model()
custom_profiles = {
    "Customers": CustomerProfile,
    "Managers": ManagerProfile,
    "Admins": AdminProfile,
}


def assign_user_to_custom_profile(user: User):
    """
    Assigns a user to their corresponding custom profile model based on group membership.

    """

    for group_name, custom_profile in custom_profiles.items():
        if user.groups.filter(name=group_name).exists():
            custom_profile.objects.get_or_create(user=user)
            break  # Stop after first matching group


def deprecated_sync_user_custom_profiles(user: User):
    """
    Ensures a user's custom profiles align with their group memberships.
    Deletes any custom profile the user should not have.
    Creates missing profile if necessary.
    """
    for group_name, custom_profile in custom_profiles.items():
        # If user has profile but not in the group -> remove it
        if (
            not user.groups.filter(name=group_name).exists()
            and custom_profile.objects.filter(user=user).exists()
        ):
            custom_profile.objects.filter(user=user).delete()
        elif (
            user.groups.filter(name=group_name).exists()
            and not custom_profile.objects.filter(user=user).exists()
        ):
            custom_profile.objects.get_or_create(user=user)


def sync_user_custom_profiles(user: User):
    """
    Synchronize a user's custom profiles with their group memberships.
    - Deletes profiles the user shouldn't have.
    - Creates profiles the user should have but doesn't.
    """
    # Cache group names once to avoid repeated DB hits
    user_group_names = set(user.groups.values_list("name", flat=True))

    for group_name, custom_profile_model in custom_profiles.items():
        has_group = group_name in user_group_names
        has_profile = custom_profile_model.objects.filter(user=user).exists()

        if has_profile and not has_group:
            # Remove profiles for groups the user is no longer in
            custom_profile_model.objects.filter(user=user).delete()

        elif has_group and not has_profile:
            # Create profile if user belongs to group but doesn't have one
            custom_profile_model.objects.get_or_create(user=user)
