# Generated by Django 3.2.5 on 2021-08-05 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0021_auto_20210805_2140'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArchivedTicket',
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
