from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.

class Deal(models.Model):
    deal_type_choice=(
        ('Purchase','Purchase'),
        ('Sale','Sale'),
        ('Refinance','Refinance'),
        ('Will','Will'),
        ('Title Transfer', 'Title Transfer'),
        ('Refuge', 'Refuge')
    )
    city_choice = (
        ('Toronto', 'Toronto'),
        ('Ottawa', 'Ottawa'),
        ('Mississauga', 'Mississauga'),
        ('Brampton', 'Brampton'),
        ('Hamilton', 'Hamilton'),
        ('London', 'London'),
        ('Markham', 'Markham'),
        ('Vaughan', 'Vaughan'),
        ('Kitchener', 'Kitchener'),
        ('Richmond Hill', 'Richmond Hill'),
    )
    province_choice=(
        ('ON','ON'),
        ('QC','QC'),
        ('NS','NS'),
        ('NB','NB'),
        ('MB','MB'),
        ('AB','AB'),
        ('BC','BC'),
    )

    st_suffix_choice=(
        ('Avenue','Avenue'),
        ('Road','Road'),
        ('Street','Street'),
        ('Blvd','Blvd'),
        ('Court','Court'),
        ('Cresent','Cresent')
    )
    current_status_choice = [
        ('client_info_required', 'client info required'),
        ('docs_sent_to_client', 'Docs are sent to Clients'),
        ('closing_ready', 'closing ready'),
        ('mtg_not_arrive_yet', 'MTG does not arrive yet'),
        ('deal_completed','Deal Completed'),

    ]


    deal_id = models.AutoField(primary_key=True)
    file_number=models.IntegerField()
    client_name=models.CharField(max_length=200)
    price=models.IntegerField(null=True, blank=True)
    client_photo1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    client_photo2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    client_photo3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    deal_type =models.TextField(choices=deal_type_choice)
    unit_number=models.IntegerField(null=True, blank=True)
    street_number=models.IntegerField()
    street_name=models.CharField(max_length=100)
    street_suffix=models.CharField(max_length=100, choices=st_suffix_choice)
    city = models.CharField(choices=city_choice, max_length=100)
    province=models.CharField(choices=province_choice, max_length=100)
    closing_date=models.DateTimeField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    status= models.TextField(choices=current_status_choice, max_length=150)
    is_deal_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name
