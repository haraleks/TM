# Generated by Django 3.1 on 2020-09-27 11:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='partevent',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
