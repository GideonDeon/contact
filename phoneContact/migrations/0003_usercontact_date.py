# Generated by Django 4.0.3 on 2022-04-21 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phoneContact', '0002_rename_contact_usercontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontact',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
