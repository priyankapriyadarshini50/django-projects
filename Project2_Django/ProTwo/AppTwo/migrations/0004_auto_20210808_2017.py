# Generated by Django 3.2.5 on 2021-08-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0003_auto_20210808_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('qualification', models.CharField(choices=[('UG', 'Under Graduate'), ('G', 'Graduate'), ('PG', 'Post Graduate'), ('PhD', 'Doctor of Philosophy')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='UsersInfo',
        ),
    ]