# Generated by Django 5.0.2 on 2024-02-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksymbol',
            name='current_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stocksymbol',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]
