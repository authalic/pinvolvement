# Generated by Django 2.0.2 on 2018-03-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20180305_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='followup',
            field=models.BooleanField(default=False),
        ),
    ]
