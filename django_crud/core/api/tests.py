from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class UserApiTestCase(APITestCase):

    def setUp(self):
        user = User(username='test_user', email='test_user@test.com')
        user.set_password('test')
        user.save()

    def test_create_user(self):
        user = User.objects.get(username='test_user')
        self.assertIsInstance(user, User)

    def test_auth(self):
        data = {}
        url = reverse('api:shoes-list')
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CategoryApiTestCase(APITestCase):

    def setUp(self):
        user = User(username='test', email='teste@test.com')
        user.set_password('test')
        user.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
