# Generated by Django 5.0.6 on 2024-06-08 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('deal_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_number', models.IntegerField()),
                ('client_name', models.CharField(max_length=200)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('client_photo1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('client_photo2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('client_photo3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('deal_type', models.TextField(choices=[('Purchase', 'Purchase'), ('Sale', 'Sale'), ('Refinance', 'Refinance'), ('Will', 'Will'), ('Title Transfer', 'Title Transfer'), ('Refuge', 'Refuge')])),
                ('unit_number', models.IntegerField(blank=True, null=True)),
                ('street_number', models.IntegerField()),
                ('street_name', models.CharField(max_length=100)),
                ('street_suffix', models.CharField(choices=[('Avenue', 'Avenue'), ('Road', 'Road'), ('Street', 'Street'), ('Blvd', 'Blvd'), ('Court', 'Court'), ('Cresent', 'Cresent')], max_length=100)),
                ('city', models.CharField(choices=[('Toronto', 'Toronto'), ('Ottawa', 'Ottawa'), ('Mississauga', 'Mississauga'), ('Brampton', 'Brampton'), ('Hamilton', 'Hamilton'), ('London', 'London'), ('Markham', 'Markham'), ('Vaughan', 'Vaughan'), ('Kitchener', 'Kitchener'), ('Richmond Hill', 'Richmond Hill')], max_length=100)),
                ('province', models.CharField(choices=[('ON', 'ON'), ('QC', 'QC'), ('NS', 'NS'), ('NB', 'NB'), ('MB', 'MB'), ('AB', 'AB'), ('BC', 'BC')], max_length=100)),
                ('closing_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.TextField(choices=[('client_info_required', 'client info required'), ('docs_sent_to_client', 'Docs are sent to Clients'), ('closing_ready', 'closing ready'), ('mtg_not_arrive_yet', 'MTG does not arrive yet'), ('deal_completed', 'Deal Completed')], max_length=150)),
                ('is_deal_closed', models.BooleanField(default=False)),
            ],
        ),
    ]