# Generated by Django 2.0.2 on 2018-03-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubinput', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publiccomment',
            name='bcookie',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]
