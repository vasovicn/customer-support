# Generated by Django 3.2.5 on 2021-08-05 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0022_auto_20210805_2149'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArchivedTicket',
        ),
        migrations.CreateModel(
            name='ArchivedTicket',
            fields=[
                ('ticket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CustomerSupport.ticket')),
                ('arh_name', models.TextField()),
                ('arh_number', models.TextField()),
                ('arh_company', models.TextField()),
                ('arh_email', models.TextField()),
                ('arh_subject', models.TextField()),
                ('arh_problem', models.TextField()),
                ('arh_date_and_time_for_callback', models.DateTimeField(blank=True, null=True)),
                ('arh_comment', models.TextField(blank=True, null=True)),
                ('arh_archive', models.BooleanField(default=False)),
            ],
            bases=('CustomerSupport.ticket',),
        ),
    ]