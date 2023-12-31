# Generated by Django 4.2.7 on 2023-11-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(verbose_name=False)),
                ('due', models.DateField()),
            ],
        ),
    ]
