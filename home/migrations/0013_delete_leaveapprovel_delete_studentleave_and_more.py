# Generated by Django 4.0.4 on 2022-04-20 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_addstudent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LeaveApprovel',
        ),
        migrations.DeleteModel(
            name='StudentLeave',
        ),
        migrations.DeleteModel(
            name='StudentOuting',
        ),
    ]