# Generated by Django 3.2.5 on 2021-08-05 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0012_auto_20210805_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['date_and_time_for_callback', 'created_date_and_time']},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='datetime',
            new_name='date_and_time_for_callback',
        ),
    ]
