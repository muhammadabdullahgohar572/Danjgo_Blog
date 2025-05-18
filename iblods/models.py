from django.db import models
from cloudinary.models import CloudinaryField 
# Create your models here.
from tinymce.models import HTMLField

class category(models.Model):
      cart_id=models.AutoField(primary_key=True)
      Tittle=models.CharField(max_length=100)
      Description=models.TextField(max_length=500)
      image=CloudinaryField('image')
      url=models.CharField(max_length=100)
      add_date = models.DateTimeField(auto_now_add=True, null=True)
      
      def __str__(self):
          return self.Tittle



class Post(models.Model):
     post_id=models.AutoField(primary_key=True)
     Tittle=models.CharField(max_length=100)
     Content=HTMLField()
     image=CloudinaryField('image')
     url=models.CharField(max_length=100)
     cart=models.ForeignKey(category, on_delete=models.CASCADE)
     