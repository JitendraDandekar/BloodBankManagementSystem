# Generated by Django 3.1.2 on 2020-10-11 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=20)),
                ('terms_condtins', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='profilePic')),
                ('per_add', models.CharField(max_length=100)),
                ('temp_add', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
