# Generated by Django 3.2.7 on 2021-09-28 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210928_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
