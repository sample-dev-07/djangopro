# Generated by Django 3.0.7 on 2020-07-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200724_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Description',
            field=models.TextField(blank=True, max_length=108),
        ),
    ]