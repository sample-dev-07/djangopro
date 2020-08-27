# Generated by Django 3.0.7 on 2020-07-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_album_musician'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('medal', models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name="person's first name")),
                ('first_name2', models.CharField(max_length=30)),
            ],
        ),
    ]