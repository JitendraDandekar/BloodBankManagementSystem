# Generated by Django 3.1.2 on 2020-10-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201012_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profilePic/profile.jpg', null=True, upload_to='profilePic/'),
        ),
    ]