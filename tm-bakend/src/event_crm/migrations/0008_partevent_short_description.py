# Generated by Django 3.1 on 2020-10-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_crm', '0007_auto_20201016_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='partevent',
            name='short_description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Короткое описание'),
        ),
    ]