from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer


# -------------------------------------------------------------
# Website HTML Views (Django Templates)
# -------------------------------------------------------------

def index(request):
    """
    Renders the Little Lemon restaurant homepage.
    """
    return render(request, 'index.html', {})


def menu_page(request):
    """
    Renders the Little Lemon restaurant menu webpage.
    """
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})


def booking_page(request):
    """
    Renders the Little Lemon restaurant table booking webpage.
    """
    return render(request, 'book.html', {})


# -------------------------------------------------------------
# Menu API Views
# -------------------------------------------------------------

class MenuItemsView(generics.ListCreateAPIView):
    """
    GET /restaurant/menu/ - List all menu items (public read)
    POST /restaurant/menu/ - Create a new menu item (authenticated users)
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /restaurant/menu/<id>/ - Retrieve a single menu item
    PUT /restaurant/menu/<id>/ - Update a menu item
    PATCH /restaurant/menu/<id>/ - Partially update a menu item
    DELETE /restaurant/menu/<id>/ - Delete a menu item
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------------------------------------------
# Booking API Views
# -------------------------------------------------------------

class BookingViewSet(viewsets.ModelViewSet):
    """
    Viewset providing full CRUD for table bookings:
    - GET /restaurant/booking/tables/
    - POST /restaurant/booking/tables/
    - GET /restaurant/booking/tables/<id>/
    - PUT /restaurant/booking/tables/<id>/
    - PATCH /restaurant/booking/tables/<id>/
    - DELETE /restaurant/booking/tables/<id>/
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# -------------------------------------------------------------
# User Registration API View
# -------------------------------------------------------------

class UserRegistrationView(generics.CreateAPIView):
    """
    POST /api/users/ or /restaurant/users/
    Registers a new user account.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
