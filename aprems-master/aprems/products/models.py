from django.db import models

# Create your models here.
class Catagery(models.Model):

    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='cat_images/')
    def __str__(self):
        return self.name