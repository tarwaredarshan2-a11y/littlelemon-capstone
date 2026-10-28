from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class MenuItem(models.Model):
    """
    Represents a dish or beverage on the Little Lemon restaurant menu.
    """
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['title']
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


# Alias for Coursera rubric compatibility
Menu = MenuItem


class Booking(models.Model):
    """
    Represents a table reservation at Little Lemon.
    """
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    booking_date = models.DateField()
    booking_time = models.TimeField(default='18:00:00')
    table_number = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    booking_reference = models.CharField(max_length=50, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['booking_date', 'booking_time']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.name} - {self.booking_date} {self.booking_time} ({self.no_of_guests} guests)'

    def save(self, *args, **kwargs):
        # Auto-generate a booking reference if not provided
        if not self.booking_reference and self.booking_date:
            if hasattr(self.booking_date, 'strftime'):
                date_str = self.booking_date.strftime('%Y%m%d')
            elif isinstance(self.booking_date, str):
                date_str = self.booking_date.replace('-', '')
            else:
                date_str = str(self.booking_date)
            short_id = uuid.uuid4().hex[:6].upper()
            self.booking_reference = f"LL-{date_str}-{short_id}"
        super().save(*args, **kwargs)
