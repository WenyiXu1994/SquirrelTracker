# Generated by Django 2.2.7 on 2019-12-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirreldata', '0004_auto_20191202_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2),
        ),
    ]
