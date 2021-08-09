# Generated by Django 3.2.5 on 2021-08-05 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0016_auto_20210805_1505'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicketsArchive',
        ),
        migrations.CreateModel(
            name='ArchivedTicket',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('CustomerSupport.ticket',),
        ),
    ]
