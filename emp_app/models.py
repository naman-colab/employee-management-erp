from django.db import models

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Employee Model
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE) 
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE) 
    phone = models.CharField(max_length=15, default="")  
    hire_date = models.DateField(blank=True, null=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
