# Generated by Django 3.1.2 on 2020-10-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201012_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
