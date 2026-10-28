from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem, Booking
from restaurant.serializers import MenuItemSerializer


class WebsiteViewsTest(TestCase):
    """
    Test suite for Little Lemon HTML template views.
    """
    def setUp(self):
        self.client = APIClient()
        self.item = MenuItem.objects.create(title="Bruschetta", price=7.99, inventory=30)

    def test_homepage_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "Little Lemon")

    def test_menu_page_view(self):
        response = self.client.get(reverse('menu-page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertContains(response, "Bruschetta")
        self.assertContains(response, "7.99")

    def test_booking_page_view(self):
        response = self.client.get(reverse('book-page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'book.html')
        self.assertContains(response, "Reserve a Table")


class MenuAPITestCase(TestCase):
    """
    Test suite for Menu API endpoints (/restaurant/menu/ and /restaurant/menu/<id>/).
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testadmin', password='Password123!')
        self.token = Token.objects.create(user=self.user)
        self.item1 = MenuItem.objects.create(title="Pizza", price=14.50, inventory=10)
        self.item2 = MenuItem.objects.create(title="Pasta", price=12.00, inventory=15)

    def test_get_all_menu_items_unauthenticated(self):
        """
        GET /restaurant/menu/ is public (read-only) and returns 200 OK.
        """
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_menu_item_unauthenticated_fails(self):
        """
        POST /restaurant/menu/ without auth should return 401 Unauthorized.
        """
        payload = {'title': 'Tiramisu', 'price': '6.50', 'inventory': 25}
        response = self.client.post('/restaurant/menu/', payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_menu_item_authenticated_succeeds(self):
        """
        POST /restaurant/menu/ with token auth creates item and returns 201 Created.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        payload = {'title': 'Tiramisu', 'price': '6.50', 'inventory': 25}
        response = self.client.post('/restaurant/menu/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Tiramisu')
        self.assertEqual(MenuItem.objects.count(), 3)

    def test_get_single_menu_item(self):
        """
        GET /restaurant/menu/<id>/ returns single menu item.
        """
        response = self.client.get(f'/restaurant/menu/{self.item1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pizza')

    def test_put_single_menu_item_authenticated(self):
        """
        PUT /restaurant/menu/<id>/ updates an item.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        payload = {'title': 'Pizza Margherita', 'price': '15.50', 'inventory': 12}
        response = self.client.put(f'/restaurant/menu/{self.item1.id}/', payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pizza Margherita')

    def test_delete_single_menu_item_authenticated(self):
        """
        DELETE /restaurant/menu/<id>/ deletes an item.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(f'/restaurant/menu/{self.item2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MenuItem.objects.filter(id=self.item2.id).exists())


class BookingAPITestCase(TestCase):
    """
    Test suite for Table Booking API endpoints (/restaurant/booking/tables/).
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='diner1', password='Password123!')
        self.token = Token.objects.create(user=self.user)
        self.booking = Booking.objects.create(
            name='Carol Danvers',
            no_of_guests=3,
            booking_date='2026-11-20',
            booking_time='19:30:00',
            table_number=5
        )

    def test_get_bookings_unauthenticated_fails(self):
        """
        GET /restaurant/booking/tables/ without auth returns 401.
        """
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_bookings_authenticated_succeeds(self):
        """
        GET /restaurant/booking/tables/ with auth returns 200.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_booking_authenticated_succeeds(self):
        """
        POST /restaurant/booking/tables/ creates a reservation and generates reference.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        payload = {
            'name': 'David Miller',
            'no_of_guests': 4,
            'booking_date': '2026-11-22',
            'booking_time': '20:00:00',
            'table_number': 8
        }
        response = self.client.post('/restaurant/booking/tables/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'David Miller')
        self.assertIsNotNone(response.data['booking_reference'])

    def test_detail_booking_and_update(self):
        """
        GET and PATCH on /restaurant/booking/tables/<id>/
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        detail_url = f'/restaurant/booking/tables/{self.booking.id}/'
        
        # GET
        get_res = self.client.get(detail_url)
        self.assertEqual(get_res.status_code, status.HTTP_200_OK)

        # PATCH
        patch_res = self.client.patch(detail_url, {'no_of_guests': 5})
        self.assertEqual(patch_res.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_res.data['no_of_guests'], 5)

        # DELETE
        del_res = self.client.delete(detail_url)
        self.assertEqual(del_res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())


class AuthenticationAPITestCase(TestCase):
    """
    Test suite for User Registration and Token Authentication endpoints.
    """
    def setUp(self):
        self.client = APIClient()

    def test_user_registration_endpoint(self):
        """
        POST /restaurant/users/ creates a new active user.
        """
        payload = {
            'username': 'newuser1',
            'email': 'newuser1@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.client.post('/restaurant/users/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser1').exists())

    def test_token_auth_login_endpoint(self):
        """
        POST /api-token-auth/ with valid credentials returns auth token.
        """
        User.objects.create_user(username='loginuser', password='MySecretPassword123')
        payload = {
            'username': 'loginuser',
            'password': 'MySecretPassword123'
        }
        response = self.client.post('/api-token-auth/', payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        token_str = response.data['token']

        # Use token to perform an authenticated action
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token_str)
        booking_res = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(booking_res.status_code, status.HTTP_200_OK)
