# Generated by Django 3.1.2 on 2020-10-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20201012_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
