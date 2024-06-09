from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    deal_id =models.IntegerField()
    user_id=models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    customer = models.CharField(max_length=250)
    deal_type = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email