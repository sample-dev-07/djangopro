# Generated by Django 3.0.7 on 2020-06-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorSolver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='ErrorPic')),
                ('name', models.TextField()),
                ('errorname', models.TextField()),
                ('solverfile', models.FileField(upload_to='SolverFile')),
            ],
        ),
    ]