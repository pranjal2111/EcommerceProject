from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

STATUS_CHOICES = [('Available', 'Available'),('Unavailable', 'Unavailable')]

status_list = [
    ("Pending","Pending"),
    ("Resolved","Resolved"),
]

class registermodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=15, unique=True)
    password=models.CharField(max_length=100)
    address=models.TextField()
    gender=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    profilepicture=models.ImageField(upload_to='photos')

    def profile_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.profilepicture.url))

    profile_photo.allow_tags = True

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images',blank=True,null=True)
    def image_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    image_photo.allow_tags = True

    price = models.FloatField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    seller=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class productimage(models.Model):
    productid=models.ForeignKey(Product,on_delete=models.CASCADE)
    pimage=models.ImageField(upload_to='product_images')
    def p_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.pimage.url))

    p_photo.allow_tags = True

class inquiry(models.Model):
    userid = models.ForeignKey(registermodel,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    address = models.TextField()
    budget = models.BigIntegerField()
    quantity = models.IntegerField()
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=40,choices=status_list,default="Pending")

class cart(models.Model):
    userid = models.ForeignKey(registermodel,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalamount = models.FloatField()
    orderstatus = models.IntegerField() # 1 - item added , 0 - item removed / order placed
    orderid = models.BigIntegerField() # 0 - default , orderid will updated when user will place order

# userid , finalbill , phone , address , paymode , timestamp , status , razor_pay_id
class ordermodel(models.Model):
   userid = models.ForeignKey(registermodel, on_delete=models.CASCADE)
   finaltotal = models.FloatField()
   phone = models.BigIntegerField()
   address = models.TextField()
   paymode = models.CharField(max_length=40)
   timestamp = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=False)
   razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)