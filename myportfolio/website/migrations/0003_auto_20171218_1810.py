# Generated by Django 2.0 on 2017-12-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20171218_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
