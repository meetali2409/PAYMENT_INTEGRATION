from django.db import models

# Create your models here.
class Apple(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    paymentid=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)