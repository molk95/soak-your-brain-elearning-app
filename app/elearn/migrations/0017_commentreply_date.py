# Generated by Django 3.1 on 2021-01-21 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0016_postcomment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]