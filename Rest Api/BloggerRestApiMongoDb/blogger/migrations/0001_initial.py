# Generated by Django 4.1.7 on 2023-04-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=70)),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
    ]
