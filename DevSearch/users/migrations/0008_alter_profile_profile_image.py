# Generated by Django 3.2.7 on 2021-10-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='images/users/'),
        ),
    ]