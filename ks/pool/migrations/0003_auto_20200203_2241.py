# Generated by Django 3.0.3 on 2020-02-03 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0002_auto_20200203_2222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PollServices',
            new_name='PoolServices',
        ),
    ]