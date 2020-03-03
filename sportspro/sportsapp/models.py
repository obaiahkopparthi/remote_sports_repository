from django.db import models
from multiselectfield import MultiSelectField

class LoginData(models.Model):
    username=models.CharField(max_length= 50)
    password=models.CharField(max_length=50)

class RegistrationData(models.Model):
    #TYPEOF_REGISTER = (
        #('coa','coach'),
        #('ump','umpire'),
        #('pla','player'),
    #)
    #typeof_register = MultiSelectField(max_length=200,type_of_register=TYPEOF_REGISTER)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    age=models.IntegerField()

class MrecordData(models.Model):
    match_name=models.CharField(max_length=50)
    match_status=models.CharField(max_length=50)
    match_coach=models.CharField(max_length=50)
    match_umpire=models.CharField(max_length=50)
    match_number=models.IntegerField()

class ReportData(models.Model):
    report_name=models.CharField(max_length=50)
    report_status=models.CharField(max_length=50)
    report_coach=models.CharField(max_length=50)
    report_umpire=models.CharField(max_length=50)
