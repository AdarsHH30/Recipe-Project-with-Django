from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recipe(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
        
    recipe_name=models.CharField(max_length=100)
    recipe_dis=models.TextField(null=True,blank=True)
    recipe_image=models.ImageField(upload_to="images",null=True,blank=True)
