from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250)
    wikipedia_link = models.URLField()
class Material(models.Model):
    name = models.CharField(max_length=250)



class Schoolstore(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    materials = models.ManyToManyField(Material)
    def __str__(self):
        return self.name
class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    def __str__(self):
        return self.username
