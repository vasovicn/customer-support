# Generated by Django 3.2.5 on 2021-08-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0009_alter_ticket_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
