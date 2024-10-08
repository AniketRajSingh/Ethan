from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'supplierprofiles', views.SupplierProfileViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'supplierratings', views.SupplierRatingViewSet)
router.register(r'complaints', views.ComplaintViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
