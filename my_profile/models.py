from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Model representing additional user profile information.

    Fields:
        user (User): The associated user.
        about_me (TextField): Text field for a user's description.
        location (CharField): String field for a user's location.
        profile_picture (CloudinaryField): Cloudinary image field for
        the user's profile picture.

    Methods:
        __str__: Returns the username of the associated user.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )

    about_me = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    profile_picture = CloudinaryField('profile_picture', default='placeholder')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to automatically create a user profile when
    a new user is created.

    Args:
        sender: The model class that sends the signal (User in this case).
        instance: The actual instance being saved.
        created (bool): True if a new instance was created,
        False if it was an update.
        kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        UserProfile.objects.create(user=instance)
