# Generated by Django 3.2.5 on 2021-08-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupport', '0004_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='company',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='datetime',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='number',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='problem',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='subject',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
