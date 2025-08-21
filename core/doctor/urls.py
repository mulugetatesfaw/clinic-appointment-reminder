from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'availability', AvailabilityViewSet)

urlpatterns = router.urls
