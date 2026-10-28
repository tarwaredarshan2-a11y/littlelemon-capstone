from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Django auth User model.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Little Lemon Menu Items.
    """
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_inventory(self, value):
        if value < 0:
            raise serializers.ValidationError("Inventory cannot be negative.")
        return value


# Alias for Coursera rubric compatibility
MenuSerializer = MenuItemSerializer


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Little Lemon Table Bookings.
    """
    class Meta:
        model = Booking
        fields = [
            'id',
            'name',
            'no_of_guests',
            'booking_date',
            'booking_time',
            'table_number',
            'booking_reference',
            'created_at',
        ]
        read_only_fields = ['id', 'booking_reference', 'created_at']

    def validate_no_of_guests(self, value):
        if value < 1 or value > 20:
            raise serializers.ValidationError("Number of guests must be between 1 and 20.")
        return value

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Name is required and cannot be blank.")
        return value.strip()
