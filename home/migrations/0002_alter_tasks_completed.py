# Generated by Django 4.2.7 on 2023-11-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
