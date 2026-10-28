from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router for Booking ViewSet
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking-tables')

urlpatterns = [
    # HTML Web Pages
    path('', views.index, name='index'),
    path('menu-view/', views.menu_page, name='menu-page'),
    path('book/', views.booking_page, name='book-page'),

    # Menu API Endpoints
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),

    # Table Booking API Endpoints: /restaurant/booking/tables/
    path('booking/', include(router.urls)),

    # User Registration API
    path('users/', views.UserRegistrationView.as_view(), name='user-register'),
]
