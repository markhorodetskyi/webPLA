# Generated by Django 2.1.4 on 2019-04-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterdataprivate',
            name='comment',
            field=models.CharField(max_length=100, null=True, verbose_name='Джерело'),
        ),
    ]
