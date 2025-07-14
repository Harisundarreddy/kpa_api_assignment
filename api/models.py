from django.db import models

# Create your models here.


class KPAFormData(models.Model):
    name = models.CharField(max_length=28)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name