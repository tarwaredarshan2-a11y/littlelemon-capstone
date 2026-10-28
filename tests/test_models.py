from django.test import TestCase
from decimal import Decimal
from restaurant.models import MenuItem, Menu, Booking
import datetime


class MenuItemModelTest(TestCase):
    """
    Tests for MenuItem (Menu) model representations and fields.
    """
    def setUp(self):
        self.item = MenuItem.objects.create(
            title="Lemon Dessert",
            price=Decimal("12.50"),
            inventory=20
        )

    def test_menu_item_str_representation(self):
        """
        Verify string representation follows Coursera specification: 'Title : Price'.
        """
        self.assertEqual(str(self.item), "Lemon Dessert : 12.50")

    def test_coursera_example_item(self):
        """
        Coursera specific rubric example: IceCream : 80
        """
        icecream = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(icecream), "IceCream : 80")

    def test_menu_alias(self):
        """
        Verify Menu alias points to MenuItem.
        """
        self.assertIs(Menu, MenuItem)

    def test_menu_item_creation(self):
        """
        Verify database fields are stored accurately.
        """
        self.assertEqual(self.item.title, "Lemon Dessert")
        self.assertEqual(self.item.price, Decimal("12.50"))
        self.assertEqual(self.item.inventory, 20)


class BookingModelTest(TestCase):
    """
    Tests for Booking model representations and auto-reference generation.
    """
    def setUp(self):
        self.booking = Booking.objects.create(
            name="Alice Smith",
            no_of_guests=4,
            booking_date=datetime.date(2026, 11, 15),
            booking_time=datetime.time(19, 0),
            table_number=3
        )

    def test_booking_str_representation(self):
        """
        Verify string representation format.
        """
        expected_str = f"Alice Smith - 2026-11-15 19:00:00 (4 guests)"
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_reference_generation(self):
        """
        Verify reference is automatically generated on save.
        """
        self.assertIsNotNone(self.booking.booking_reference)
        self.assertTrue(self.booking.booking_reference.startswith("LL-20261115-"))
