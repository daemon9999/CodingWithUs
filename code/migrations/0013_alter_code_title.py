# Generated by Django 3.2.5 on 2022-04-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code', '0012_auto_20220418_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
