from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=100,default="")
    product_price = models.IntegerField(default=0)
    author = models.CharField(max_length=100,default="")
    product_desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", blank=True, null=True)

    def __str__(self):
        return self.product_name 
    
class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.TextField(max_length=5000, default="")
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=20, default="")
    
    def __str__(self):
        return self.name
    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=500, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."  # Return first 7 characters of update_desc