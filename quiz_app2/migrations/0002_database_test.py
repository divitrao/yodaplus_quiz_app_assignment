# Generated by Django 3.0.7 on 2021-09-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='database_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=100)),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
            ],
        ),
    ]
