# Generated by Django 4.0.3 on 2022-04-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneContact', '0003_usercontact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
