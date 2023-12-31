from django.db import models

# Create your models here.
# import datetime
# import os
# def filepath(request,filename):
#     old_filename=filename
#     timenow=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     filename="%s%s",(timenow,old_filename)
#     return os.path.join('uploads/',filename)


class Addproduct(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=30 ,null=True)
    image=models.ImageField(upload_to='media/')
    price=models.IntegerField()
    details=models.CharField(max_length=50)



class User(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=30,null=True)
    image=models.ImageField()
    price=models.IntegerField()
    details=models.CharField(max_length=50)

class review(models.Model):
    n=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    comment=models.CharField(max_length=50)


class register(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    copassword=models.CharField(max_length=20)




