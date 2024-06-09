# Generated by Django 5.0.6 on 2024-06-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='customer',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='deal_type',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=250),
        ),
    ]