from django.db.models.signals import m2m_changed, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import logging
from django.core.exceptions import PermissionDenied


User = get_user_model()
logger = logging.getLogger(__name__)

from .utils import sync_user_custom_profiles


@receiver(m2m_changed, sender=User.groups.through)
def sync_profiles_on_group_change(sender, instance, action, **kwargs):
    """
    Syncs a user's custom profiles whenever their group memberships change.
    """
    if action in {"post_add", "post_remove", "post_clear"}:
        sync_user_custom_profiles(instance)


@receiver(pre_delete, sender=User)
def prevent_deletion_of_protected_users(sender, instance, using, **kwargs):
    """
    Prevent deletion of protected (fallback/main_admin) users.
    """
    protected_users = {"manager_Abe", "kutologojm"}

    if instance.username in protected_users:
        logger.warning(
            f"Attempted to delete protected user '{instance.username}' — blocked."
        )
        raise PermissionDenied(
            f"You cannot delete the protected user '{instance.username}'."
        )
