# Generated by Django 3.1 on 2020-08-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('elearn', '0008_auto_20200821_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classtestpost',
            name='student',
        ),
        migrations.AddField(
            model_name='classtestpost',
            name='student',
            field=models.ManyToManyField(blank=True, to='elearn.Student'),
        ),
    ]
