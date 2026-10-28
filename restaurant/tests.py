# Import all test cases so they are discovered by `python manage.py test restaurant`
from tests.test_models import MenuItemModelTest, BookingModelTest
from tests.test_serializers import SerializerTestCase
from tests.test_views import (
    WebsiteViewsTest,
    MenuAPITestCase,
    BookingAPITestCase,
    AuthenticationAPITestCase,
)
