from django.db import models
from . constant import gender_choices
# Create your models here.



class CustomerAccount (models.Model):
    username = models.CharField (max_length=50)
    password = models.CharField (max_length=50)
    first_name  = models.CharField(max_length=200,)
    last_name =  models.CharField(max_length=200)
    email = models.EmailField ()
    Tel = models.IntegerField()
    DOB = models.DateField()

class ReservationRecord (models.Model):
    Cu_no = models.ForeignKey(CustomerAccount,on_delete=models.CASCADE)


class ResturantTable (models.Model):
    Status = models.BooleanField()


class ResturantSeats (models.Model):
    TableNum = models.ForeignKey(ResturantTable,on_delete=models.CASCADE)
    seatsNum = models.OneToOneField(ReservationRecord,on_delete=models.CASCADE)


class Employee (models.Model):
    first_name = models.CharField (max_length=50)
    last_name = models.CharField (max_length=50)
    gender = models.name = models.CharField(max_length=200, choices = gender_choices)
    DOB = models.DateField()
    email = models.EmailField()
    Tel = models.PositiveIntegerField()
    Salary = models.PositiveIntegerField()

class MenuRecord (models.Model):
    Name = models.CharField(max_length=200)
    Img = models.ImageField()
    Des = models.TextField()
    Ingredients = models.TextField()
    Promotion = models.IntegerField()
    Price = models.PositiveIntegerField()

class OrderRecord (models.Model):
    OrderID = models.IntegerField()
    MenuID = models.ForeignKey(MenuRecord,on_delete=models.CASCADE)
    TableNum = models.IntegerField()   
    Order_time = models.DateField()
    E_id = models.ForeignKey(Employee,on_delete=models.CASCADE) 





