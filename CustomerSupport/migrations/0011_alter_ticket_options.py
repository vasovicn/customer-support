# Generated by Django 3.2.5 on 2021-08-05 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0010_ticket_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['datetime', 'created_date']},
        ),
    ]
