from django.contrib import admin
from .models import UserProfile, SupplierProfile, Order, Subscription, SupplierRating, Complaint

# Register UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_number', 'address')
    search_fields = ('email__username', 'name', 'phone_number')

# Register SupplierProfile
@admin.register(SupplierProfile)
class SupplierProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'company_name', 'contact_number', 'address', 'gst_number')
    search_fields = ('email__username', 'company_name', 'contact_number', 'gst_number')

# Register Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'supplier', 'quantity', 'cost_of_items', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    search_fields = ('user__email__username', 'supplier__company_name')

# Register Subscription
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscription_type', 'start_date', 'end_date')
    list_filter = ('subscription_type',)
    search_fields = ('email__email__username',)

# Register SupplierRating
@admin.register(SupplierRating)
class SupplierRatingAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'rating', 'email', 'review')
    list_filter = ('rating',)
    search_fields = ('supplier__company_name', 'email__email__username')

# Register Complaint
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('rating', 'description', 'complaint_date')
    search_fields = ('rating__supplier__company_name', 'description')
