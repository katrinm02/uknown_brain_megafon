# Generated by Django 3.0.3 on 2020-02-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollServices',
            fields=[
                ('ticket', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('endpoint', models.URLField()),
                ('pool', models.IntegerField()),
                ('state', models.CharField(default='STATE_AVAILABLE', max_length=50)),
                ('timestampt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PoopPending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer', models.DateTimeField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool.PollServices')),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
