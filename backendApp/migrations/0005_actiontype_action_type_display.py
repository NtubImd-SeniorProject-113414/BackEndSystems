# Generated by Django 5.1 on 2024-09-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backendApp", "0004_alter_turnpoint_qr_point"),
    ]

    operations = [
        migrations.AddField(
            model_name="actiontype",
            name="action_type_display",
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
