# Generated by Django 4.0.4 on 2022-04-20 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_studentleave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentleave',
            name='date_of_outing',
        ),
    ]
