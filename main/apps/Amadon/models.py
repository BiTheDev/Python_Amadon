from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)