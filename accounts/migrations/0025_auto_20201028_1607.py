# Generated by Django 3.1.2 on 2020-10-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20201028_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='req_date',
            field=models.DateTimeField(),
        ),
    ]
