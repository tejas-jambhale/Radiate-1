# Generated by Django 3.0.5 on 2020-05-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20200505_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='score',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]