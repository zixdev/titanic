from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='admin123456'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='test123456',
            name="Tester"
        )

    def test_users_listed(self):
        """It Should Show users list page"""
        url = reverse('admin:users_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """It Should Show The User Edit Page"""
        url = reverse('admin:users_user_change', args=[self.user.id])
        rest = self.client.get(url)

        self.assertEqual(rest.status_code, 200)

    def test_create_user_page(self):
        """It Should Confirm That The User Page Works"""
        url = reverse('admin:users_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
