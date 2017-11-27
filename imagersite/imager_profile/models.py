"""Imager Profile model."""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ImagerProfile(models.Model):
    """Creates a ImaderProfile class."""

    SLR = 'SLR'
    NIKON = 'Nikon'
    CANNON = 'Cannon'
    DIGITAL = 'Digital'
    ANALOG = 'Analog'
    CAMERA_CHOICES = (
        (SLR, 'SLR'),
        (NIKON, 'Nikon'),
        (CANNON, 'Cannon'),
        (DIGITAL, 'Digital'),
        (ANALOG, 'Analog'),
    )
    WEDDING = 'Wedding'
    SENIOR = 'Senior Photos'
    FAMILY = 'Family Photos'
    SPORTS = 'Sports Photography'
    LANDSCAPE = 'City and Rural Landscapes'
    SERVICES = (
        (WEDDING, 'Wedding'),
        (SENIOR, 'Senior Pictures'),
        (FAMILY, 'Family Photos'),
        (SPORTS, 'Sports Photo'),
        (LANDSCAPE, 'Landscapes'),
    )
    BW = 'Black and White'
    COLOR = 'Color'
    PS = 'Photoshop Ability'
    STYLES = (
        (BW, 'BW'),
        (COLOR, 'Color'),
        (PS, 'Photoshop'),
    )

    website = models.CharField(max_length=180, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    fee = models.FloatField(max_length=20, blank=True, null=True)
    camera = models.CharField(max_length=50, choices=CAMERA_CHOICES, blank=True, null=True)
    services = models.CharField(max_length=50, choices=SERVICES, blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo_styles = models.CharField(max_length=50, choices=STYLES, blank=True, null=True)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User)

    def active(self):
        """Return active users."""
        return [user.username for user in User.objects.all() if user.is_active]


@receiver(post_save, sender=User)
def create_user_imager_profile(sender, instance, created, **kwargs):
    """Create a profile."""
    if created:
        ImagerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_imager_profile(sender, instance, **kwargs):
    """Save user profile."""
    instance.profile.save()
