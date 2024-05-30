from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# from multiselectfield import MultiSelectField
# Create your models here.

class Transaction(models.Model):
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
        ('ON','Ontario'),
        ('QC','Quebec'),
        ('NS','Nova Scotia'),
        ('NB','New Brunswick'),
        ('MB','Manitoba'),
        ('AB','Alberta'),
        ('BC','British Columbia'),
    )

    st_suffix_choice=(
        ('Avenue','Avenue'),
        ('Road','Road'),
        ('Street','Street'),
        ('Blvd','Blvd'),
        ('Court','Court'),
        ('Cresent','Cresent')
    )



    closing_year_choice=[]
    for closing_year in range(2000,(datetime.now().year+5)):
        closing_year_choice.append((closing_year,closing_year))

    closing_month_choice = []
    for closing_month in range(1, 13):
        closing_month_choice.append((closing_month, closing_month))

    closing_date_choice = []
    for closing_date in range(1, 32):
        closing_date_choice.append((closing_date, closing_date))

    file_number=models.IntegerField(primary_key=True, verbose_name='File Number')
    client_name=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    client_photo1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    client_photo2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    client_photo3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    deal_type =models.TextField(choices=deal_type_choice)
    unit_number=models.IntegerField(default=0)
    street_number=models.IntegerField(default=0)
    street_name=models.CharField(max_length=100)
    street_suffix=models.CharField(max_length=100, choices=st_suffix_choice)
    city = models.CharField(choices=city_choice, max_length=100)
    province=models.CharField(choices=province_choice, max_length=100)
    closing_year = models.IntegerField(choices= closing_year_choice, default=2001)
    closing_month = models.IntegerField( choices=closing_month_choice, default=datetime.now().month)
    closing_date = models.IntegerField(choices=closing_date_choice,  default=1)
    outstanding=RichTextField()
    dialog=RichTextField()
    is_deal_closed=models.BooleanField(max_length=100, default='No')
    created_date= models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.client_name
