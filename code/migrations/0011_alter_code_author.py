# Generated by Django 3.2.5 on 2022-04-08 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('code', '0010_alter_comment_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to=settings.AUTH_USER_MODEL),
        ),
    ]
