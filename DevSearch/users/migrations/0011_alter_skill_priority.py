# Generated by Django 3.2.7 on 2021-10-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_social_gmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
