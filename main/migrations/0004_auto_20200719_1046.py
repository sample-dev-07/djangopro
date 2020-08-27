# Generated by Django 3.0.7 on 2020-07-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200623_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('errorname', models.TextField(blank=True)),
                ('solverfile', models.FileField(null=True, upload_to='SolverFile')),
            ],
        ),
        migrations.CreateModel(
            name='Django_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=50, verbose_name='Name')),
                ('projectfile', models.FileField(null=True, upload_to='ProFile')),
            ],
        ),
        migrations.DeleteModel(
            name='ErrorSolver',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
