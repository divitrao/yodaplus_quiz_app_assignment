# Generated by Django 3.0.7 on 2021-08-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='score',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
