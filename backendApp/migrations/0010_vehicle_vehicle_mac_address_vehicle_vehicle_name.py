# Generated by Django 4.2.6 on 2024-09-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0009_rename_patients_routecondition_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_mac_address',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]