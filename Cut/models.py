from django.db import models

# Create your models here.
class Search_List(models.Model):
    list_id=models.AutoField
    list_name=models.CharField(max_length=50,default="")
    Cal=models.CharField(max_length=50,default="")
    Protein=models.CharField(max_length=50,default="")
    Carb=models.CharField(max_length=50,default="")
    Fat=models.CharField(max_length=50,default="")
    Fiber=models.CharField(max_length=50,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to='List',default="")

    def __str__(self):
        return self.list_name