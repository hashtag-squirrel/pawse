# Generated by Django 3.2.20 on 2023-08-23 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20230823_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'ordering': ['order']},
        ),
    ]
