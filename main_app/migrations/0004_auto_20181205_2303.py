# Generated by Django 2.1.3 on 2018-12-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20181204_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
