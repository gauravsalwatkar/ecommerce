from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    product_name = models.CharField(max_length=200, null=False)
    product_price = models.FloatField(null=False)
    discount_price = models.FloatField(default="As per Real Price")
    product_category=models.CharField(max_length=200 ,null=False)
    description = models.TextField(default="ADD PRODUCT DESCRIPTION")
    product_image = models.ImageField(default='', upload_to="products/images")
    add_time = models.DateField(default=timezone.now)

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    phone= models.CharField(max_length=1000, default='0')
    zip_code = models.CharField(max_length=150)
    total = models.CharField(max_length=500,default=0)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profilepic.jpg",upload_to="products/profile")
    about_you = models.CharField(default="Tell us about You",max_length = 500)    
    def __str__(self):
        return str(self.user)
    
