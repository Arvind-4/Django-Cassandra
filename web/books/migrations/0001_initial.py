# Generated by Django 3.2 on 2022-04-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
            ],
            options={
                'db_table': 'books',
                'ordering': ('title',),
                'managed': False,
            },
        ),
    ]