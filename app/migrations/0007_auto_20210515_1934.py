# Generated by Django 3.2 on 2021-05-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210515_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green'), ('white', 'White'), ('black', 'Black')], default='blue', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
