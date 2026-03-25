from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='students/', null=True,blank=True)

class Feedback(models.Model):
    email = models.EmailField(null=False)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
