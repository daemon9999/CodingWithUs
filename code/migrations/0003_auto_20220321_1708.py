# Generated by Django 3.2.5 on 2022-03-21 13:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code', '0002_alter_code_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='code',
            name='code_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
