# Generated by Django 3.2.5 on 2021-08-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_basic', '0002_alter_schoolinfo_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfo',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]