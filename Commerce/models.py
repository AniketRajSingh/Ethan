from django.db import models
from django.contrib.auth.models import User

# User Profile Model
class UserProfile(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email.username

# Supplier Profile Model
class SupplierProfile(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)

    def __str__(self):
        return self.company_name

# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=15)
    user_address = models.CharField(max_length=255) 
    order_type = models.CharField(max_length=100) 
    order_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField() 
    quantity = models.IntegerField()
    cost_of_items = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.id} by {self.user.email.username}"

# Subscription Model
class Subscription(models.Model):
    SUBSCRIPTION_TYPES = [
        ('3_month', '3 Months'),
        ('6_month', '6 Months'),
        ('9_month', '9 Months'),
        ('annual', 'Annual'),
    ]
    email = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=10, choices=SUBSCRIPTION_TYPES)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField() 

    def __str__(self):
        return f"{self.email.name} - {self.subscription_type}"

# Supplier Ratings Model
class SupplierRating(models.Model):
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    email = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating for {self.supplier.company_name} by {self.email.name}"

# Complaint Model
class Complaint(models.Model):
    rating = models.ForeignKey(SupplierRating, on_delete=models.CASCADE)
    description = models.TextField()
    complaint_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint for Rating {self.rating.id}"
