"""Imager Profile model."""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class User(User, PermissionsMixin):
#     """Create an new User class."""

#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     email = models.EmailField(max_length=100, blank=True)
#     is_staff = models.BooleanField(
#         default=False,
#         help_text=('Designates whether the user can log into this admin site.'),
#     )
#     is_active = models.BooleanField(
#         default=True,
#         help_text=(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#     date_joined = models.DateTimeField(default=timezone.now)


class ImagerProfile(models.Models):
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
    user = models.ForeignKey(User, unique=True)
