# Generated by Django 3.0.6 on 2020-07-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_donate_total_donate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total_donate',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]