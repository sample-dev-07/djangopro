from django.db import models

# Create your models here.
class Application(models.Model):
    Title = models.CharField(max_length=50,primary_key=True)
    Description = models.TextField(blank=True, max_length=108)
    PythonFile = models.FileField(upload_to="Python",null=True)
    ExeFile = models.FileField(upload_to="Application",null=True)

class Django_Project(models.Model):
    ProjectName = models.CharField(("Name"), max_length=50,primary_key=True)
    Description = models.TextField(blank=True)
    ProjectFolder = models.FileField(upload_to="ProFile",null=True)

class Hacking(models.Model):
    FileName = models.CharField(("Name"), max_length=50,primary_key=True)
    Working = models.TextField(blank=True)
    File = models.FileField(upload_to="ProFile",null=True)

# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)

# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()

# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

# class Runner(models.Model):
#     MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
#     name = models.CharField(max_length=60)
#     medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

# class Fruit(models.Model):
#     name = models.CharField(max_length=100, primary_key=True)

# class test(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField("person's first name", max_length=30)
#     first_name2 = models.CharField(max_length=30)

