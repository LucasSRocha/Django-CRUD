from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from core.api.serializers import ShoeSerializer

from core.models import Shoes
from core.models import Categories

from django.contrib.auth import get_user_model

User = get_user_model()


class UserApiTestCase(APITestCase):

    def setUp(self):
        self.username = 'test_user'

        self.email = 'test_user@test.com'

        self.password = 'test'

        user = User(username=self.username, email=self.email)

        user.set_password(self.password)

        user.save()

    def test_created_user(self):
        user = User.objects.get(username=self.username)

        self.assertIsInstance(user, User)

    def test_unauthorized(self):
        data = {}

        url = reverse('api:shoes-list')

        resp = self.client.get(url, data=data)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login(self):
        data = {
            'username': self.username,

            'password': self.password,
        }

        url = reverse('api_login')

        resp = self.client.post(url, data=data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class CategoryApiTestCase(APITestCase):

    def setUp(self):
        self.username = 'testcategory'

        self.email = 'category@test.com'

        self.password = 'test'

        user = User(username=self.username, email=self.email)

        user.set_password(self.password)

        user.save()

        self.data = {'username': self.username, 'password': self.password}

        resp = self.client.post(reverse('api_login'), data=self.data)

        self.client.credentials(HTTP_AUTHORIZATION=f"{api_settings.JWT_AUTH_HEADER_PREFIX} {resp.data['token']}")

    def test_list(self):
        url = reverse('api:category-list')

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertEqual(resp.data.get('count'), 0)

    def test_create(self):
        url = reverse('api:category-list')

        data = {"category": "create-test-category"}

        resp = self.client.post(url, data=data)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        category = Categories.objects.create(category='change-me-category')

        url = reverse('api:category-detail', args=[category.id])

        new_category = 'update-test-category'

        data = {"id": category.id, 'category': new_category}

        resp = self.client.put(url, data=data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        check_category = Categories.objects.get(id=category.id)

        self.assertEqual(check_category.category, new_category)

    def test_delete(self):
        category = Categories.objects.create(category='category-to-be-deleted')

        url = reverse('api:category-detail', args=[category.id])

        data = {'id': category.id}

        resp = self.client.delete(url, data=data)

        self.assertEqual(len(Categories.objects.all()), 0)

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)


class ShoesApiTestCase(APITestCase):

    def setUp(self):
        self.username = 'testshoes'

        self.email = 'shoes@test.com'

        self.password = 'test'

        user = User(username=self.username, email=self.email)

        user.set_password(self.password)

        user.save()

        self.data = {'username': self.username, 'password': self.password}

        resp = self.client.post(reverse('api_login'), data=self.data)

        self.client.credentials(HTTP_AUTHORIZATION=f"{api_settings.JWT_AUTH_HEADER_PREFIX} {resp.data['token']}")

        category = Categories.objects.create(category='Unisex')

        self.shoe_data = {
            "price": 10.99,
            "size": "37",
            "color": "Blue",
            "shoes_stock": 100,
            "shoes_bought": 0,
            "shoe_model": "Rad Sports",
            "shoe_brand": "Sadida",
            "class_category": [category.id]
            }

    def test_list(self):
        url = reverse('api:shoes-list')

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertEqual(resp.data.get('count'), 0)

    def test_create(self):
        url = reverse('api:shoes-list')

        resp = self.client.post(url, data=self.shoe_data)

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        serializer = ShoeSerializer()

        shoe = serializer.create(self.shoe_data)

        url = reverse('api:shoes-detail', args=[shoe.id])

        data = {"id": shoe.id, 'shoe_brand': 'Sanaiavah', 'shoe_model': 'satagralA'}

        resp = self.client.put(url, data=data)

        self.assertEqual(resp.status_code, status.HTTP_202_ACCEPTED)

        check_shoe = Shoes.objects.get(id=shoe.id)

        self.assertEqual(check_shoe.shoe_brand, 'Sanaiavah')

        self.assertEqual(check_shoe.shoe_model, 'satagralA')

    def test_delete(self):
        serializer = ShoeSerializer()
        shoe = serializer.create(self.shoe_data)

        url = reverse('api:shoes-detail', args=[shoe.id])

        data = {'id': shoe.id}

        resp = self.client.delete(url, data=data)

        self.assertEqual(len(Shoes.objects.all()), 0)

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)


