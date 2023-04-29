from django.db import models

# Create your models here.
class Cards(models.Model):
    Title = models.CharField(max_length=50,name="Title")
    SubTitle = models.CharField(max_length=50,name="SubTitle")
    Description = models.TextField(max_length=500,name="Description")
    Image = models.CharField(max_length=50,name="Image",default="")

    def getImage(self):
        return '/imgs/' + self.Image


class Journal(models.Model):
    image = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=500)

    def GetImageName(self):
        return '/imgs/' + self.image

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    


