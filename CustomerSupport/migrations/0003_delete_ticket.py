# Generated by Django 3.2.5 on 2021-08-04 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0002_rename_tickets_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
