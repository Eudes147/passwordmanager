from django.db import models

# Create your models here.
class PasswordManager(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=100)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.name