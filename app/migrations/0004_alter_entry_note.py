# Generated by Django 3.2 on 2021-05-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_entry_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='note',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
