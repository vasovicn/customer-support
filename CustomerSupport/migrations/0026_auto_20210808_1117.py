# Generated by Django 3.2.5 on 2021-08-08 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0025_delete_archivedticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['date_and_time_for_callback', 'submitted_date_and_time']},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='submited_date_and_time',
            new_name='submitted_date_and_time',
        ),
    ]
