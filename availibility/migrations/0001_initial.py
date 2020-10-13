# Generated by Django 3.1.2 on 2020-10-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodAvailibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('blood_a', models.IntegerField()),
                ('blood_b', models.IntegerField()),
                ('blood_ab', models.IntegerField()),
                ('blood_o', models.IntegerField()),
                ('plasma', models.IntegerField()),
                ('platelet', models.IntegerField()),
            ],
        ),
    ]