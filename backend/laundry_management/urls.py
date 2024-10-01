from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LaundryClothViewSet, LaundryEventViewSet

router = DefaultRouter()

router.register(prefix='clothes', viewset=LaundryClothViewSet, basename='clothes')
router.register(prefix='events', viewset=LaundryEventViewSet, basename='events')

urlpatterns = router.urls
