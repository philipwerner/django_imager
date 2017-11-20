"""Test module for Imager."""
from django.test import TestCase
from lender_profile.models import ImagerProfile, User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'dan{n}')
    email = 'dan@theman.com'

# Create your tests here.


class ProfileTests(TestCase):
    def setUp(self):
        profile = ImagerProfile(location='nowhere')
        for i in range(50):
            user = UserFactory.create()
            user.set_password('danisinsecure')
            user.save()

        profile.user = user
        profile.save()

    def test_user_can_point_to_its_profile(self):
        one_user = User.objects.get(id=50)
        self.assertIsNotNone(one_user.profile)