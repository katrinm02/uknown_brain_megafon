# Generated by Django 3.0.3 on 2020-02-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool_2', '0002_resultpoolservice_pool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolcompare',
            name='result_pool',
            field=models.IntegerField(),
        ),
    ]
