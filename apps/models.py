from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    addrees = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to='media')
    numbers = models.IntegerField()
