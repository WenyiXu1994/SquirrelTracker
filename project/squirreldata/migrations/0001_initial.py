# Generated by Django 2.2.7 on 2019-11-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(help_text='Numerical longitude value', max_length=17)),
                ('latitude', models.CharField(help_text='Numerical latitude value', max_length=17)),
                ('unique_squirrel_id', models.CharField(help_text="Identification tag for each squirrel sightings. The tag is comprised of 'Hectare ID' + 'Shift' + 'Date(month+day)' + 'Hectare Squirrel Number'. E.g. 42C-AM-1007-02", max_length=14, unique=True)),
                ('shift', models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], max_length=2)),
                ('date', models.CharField(help_text='Concatenation of the sighting session month, day and year. E.g. 10142018', max_length=8)),
                ('Age', models.CharField(blank=True, choices=[('juvenile', 'Juvenile'), ('adult', 'Adult')], max_length=8, null=True)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('black', 'Black')], max_length=8, null=True)),
                ('location', models.CharField(blank=True, choices=[('ground plane', 'Ground Plane'), ('above ground', 'Above Ground')], max_length=12, null=True)),
                ('specific_location', models.TextField(blank=True, help_text='Specific place where squirrel was sighted. E.g. crossing street', max_length=255)),
                ('running', models.BooleanField()),
                ('chasing', models.BooleanField()),
                ('climbing', models.BooleanField()),
                ('eating', models.BooleanField()),
                ('foraging', models.BooleanField()),
                ('other_activities', models.TextField(blank=True, help_text="Activities haven't been listed. E.g. digging", max_length=255)),
                ('kuks', models.BooleanField()),
                ('quaas', models.BooleanField()),
                ('moans', models.BooleanField()),
                ('tail_flags', models.BooleanField()),
                ('tail_twitches', models.BooleanField()),
                ('approaches', models.BooleanField()),
                ('indifferent', models.BooleanField()),
                ('runs_from', models.BooleanField()),
            ],
        ),
    ]
