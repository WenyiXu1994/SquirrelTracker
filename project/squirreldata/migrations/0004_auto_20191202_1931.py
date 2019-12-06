# Generated by Django 2.2.7 on 2019-12-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirreldata', '0003_auto_20191201_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='age',
            field=models.CharField(blank=True, choices=[('Juvenile', 'Juvenile'), ('Adult', 'Adult')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground plane', 'Ground Plane'), ('Above ground', 'Above Ground')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='primary_fur_color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('Am', 'AM'), ('Pm', 'PM')], max_length=2),
        ),
    ]
