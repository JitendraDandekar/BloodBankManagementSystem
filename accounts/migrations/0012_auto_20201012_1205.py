# Generated by Django 3.1.2 on 2020-10-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201012_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.AddField(
            model_name='member',
            name='member_id',
            field=models.AutoField(default=True, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
