# Generated by Django 4.1.3 on 2022-12-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='users/'),
        ),
    ]
