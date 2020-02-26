from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """It Should create a new user with email"""
        email = 'test@test.com'
        password = 'test123456'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """It Should Normalize User Email"""
        email = 'test@TEST.com'
        password = 'test123456'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """It Should Validate The Email Address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123456')

    def test_create_new_superuser(self):
        """It Should Be Able To Create Super User"""
        user = get_user_model().objects.create_superuser(
            'admin@admin.com',
            'admin123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
