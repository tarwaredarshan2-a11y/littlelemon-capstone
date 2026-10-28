from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem, Booking
import datetime


class Command(BaseCommand):
    help = 'Seeds initial sample data for Little Lemon restaurant'

    def handle(self, *args, **options):
        # 1. Create default admin / reviewer user if not exists
        username = 'admin'
        email = 'admin@littlelemon.com'
        password = 'LittleLemonAdmin2024!'

        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        if created:
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created default admin user: '{username}' with password: '{password}'"))
        else:
            self.stdout.write(f"Admin user '{username}' already exists.")

        # Ensure auth token exists for admin
        token, _ = Token.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS(f"Reviewer Token: {token.key}"))

        # 2. Seed initial Menu Items
        menu_items = [
            {'title': 'Greek Salad', 'price': 12.99, 'inventory': 25},
            {'title': 'Bruschetta', 'price': 7.99, 'inventory': 40},
            {'title': 'Lemon Dessert', 'price': 8.50, 'inventory': 15},
            {'title': 'Grilled Fish', 'price': 19.95, 'inventory': 20},
            {'title': 'Pasta Alfredo', 'price': 14.50, 'inventory': 30},
            {'title': 'Mediterranean Pizza', 'price': 16.00, 'inventory': 18},
        ]

        for item_data in menu_items:
            item, was_created = MenuItem.objects.get_or_create(
                title=item_data['title'],
                defaults={'price': item_data['price'], 'inventory': item_data['inventory']}
            )
            if was_created:
                self.stdout.write(f"Added Menu Item: {item.title} (${item.price})")

        # 3. Seed initial Sample Booking
        booking_data = {
            'name': 'Coursera Reviewer',
            'no_of_guests': 2,
            'booking_date': datetime.date.today() + datetime.timedelta(days=1),
            'booking_time': datetime.time(19, 0),
            'table_number': 1
        }
        booking, b_created = Booking.objects.get_or_create(
            name=booking_data['name'],
            booking_date=booking_data['booking_date'],
            booking_time=booking_data['booking_time'],
            defaults=booking_data
        )
        if b_created:
            self.stdout.write(self.style.SUCCESS(f"Added sample reservation for {booking.name}. Reference: {booking.booking_reference}"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
