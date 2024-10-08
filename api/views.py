from rest_framework import viewsets
from Commerce.models import UserProfile, SupplierProfile, Order, Subscription, SupplierRating, Complaint
from .serializers import UserProfileSerializer, SupplierProfileSerializer, OrderSerializer, SubscriptionSerializer, SupplierRatingSerializer, ComplaintSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class SupplierProfileViewSet(viewsets.ModelViewSet):
    queryset = SupplierProfile.objects.all()
    serializer_class = SupplierProfileSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SupplierRatingViewSet(viewsets.ModelViewSet):
    queryset = SupplierRating.objects.all()
    serializer_class = SupplierRatingSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
