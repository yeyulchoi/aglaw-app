# Generated by Django 5.0.6 on 2024-05-28 00:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='client_photo1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='client_photo2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='client_photo3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='deal_type',
            field=models.TextField(choices=[('Purchase', 'Purchase'), ('Sale', 'Sale'), ('Refinance', 'Refinance'), ('Will', 'Will'), ('Title Transfer', 'Title Transfer'), ('Refuge', 'Refuge')]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='dialog',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='outstanding',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
    ]
