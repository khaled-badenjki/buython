# Generated by Django 3.1.2 on 2020-10-09 11:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201008_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
    ]
