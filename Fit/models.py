from django.db import models

# Create your models here.
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=13)
    adress= models.CharField(max_length=255)
    desc= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
         return self.name

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='',default="")
    def __str__(self):
        return self.product_name