from django.test import TestCase
from restaurant.models import MenuItem, Booking
from restaurant.serializers import MenuItemSerializer, BookingSerializer
import datetime


class SerializerTestCase(TestCase):
    """
    Unit tests for model serializers and data validations.
    """
    def test_menu_item_serializer_valid_data(self):
        data = {'title': 'Greek Salad', 'price': '8.50', 'inventory': 15}
        serializer = MenuItemSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        item = serializer.save()
        self.assertEqual(item.title, 'Greek Salad')

    def test_menu_item_serializer_invalid_price(self):
        data = {'title': 'Greek Salad', 'price': '-1.00', 'inventory': 15}
        serializer = MenuItemSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

    def test_menu_item_serializer_invalid_inventory(self):
        data = {'title': 'Greek Salad', 'price': '8.50', 'inventory': -5}
        serializer = MenuItemSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('inventory', serializer.errors)

    def test_booking_serializer_valid_data(self):
        data = {
            'name': 'Bob Johnson',
            'no_of_guests': 2,
            'booking_date': '2026-12-01',
            'booking_time': '18:30:00',
            'table_number': 2,
        }
        serializer = BookingSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_booking_serializer_invalid_guests(self):
        # Exceeds max guest limit of 20
        data = {
            'name': 'Party of 30',
            'no_of_guests': 30,
            'booking_date': '2026-12-01',
            'booking_time': '18:30:00'
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('no_of_guests', serializer.errors)

    def test_booking_serializer_empty_name(self):
        data = {
            'name': '   ',
            'no_of_guests': 2,
            'booking_date': '2026-12-01',
            'booking_time': '18:30:00'
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
