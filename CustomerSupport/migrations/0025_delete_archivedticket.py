# Generated by Django 3.2.5 on 2021-08-07 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0024_auto_20210805_2313'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArchivedTicket',
        ),
    ]