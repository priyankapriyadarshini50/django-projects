# Generated by Django 3.2.5 on 2021-08-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.URLField(blank=True, max_length=100, null=True)),
                ('languages', models.CharField(blank=True, max_length=60, null=True)),
                ('contact_number', models.IntegerField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('zip', models.PositiveIntegerField(max_length=50)),
            ],
        ),
    ]
