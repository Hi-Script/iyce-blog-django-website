# Generated by Django 4.1.2 on 2022-12-25 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iycee', '0007_profile_email_profile_fullname_profile_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userAccount',
        ),
    ]
