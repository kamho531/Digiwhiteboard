from django.db import models
from datetime import date

# Create your models here.

class Patients(models.Model):
    firstname = models.CharField('First Name', max_length=30)
    lastname = models.CharField('Last Name', max_length=30)
    hsnnum = models.CharField('HSN', max_length=15)
    ruhnum = models.CharField('RUH Number', max_length=15)
    dob = models.DateField('Date of Birth')
    gender = models.CharField('Gender', max_length=15)
    location = models.CharField('Location', max_length=15)
    status = models.CharField('Status', max_length=15)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    @property
    def calculateAge(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age



class Doctors(models.Model):
    firstname = models.CharField('First Name', max_length=30)
    lastname = models.CharField('Last Name', max_length=30)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Procedures(models.Model):
    proname = models.CharField('Procedure Name', max_length=30)
    diagnosis = models.CharField('Diagnosis', max_length=50)
    comments = models.CharField('Comments', max_length=120)
    admissiondate = models.DateField('Admission Date')
    xray = models.CharField(max_length=15)
    site = models.CharField(max_length=15)
    surgerydate = models.DateField('Surgery Date')
    patient = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.proname + ' ' + self.diagnosis


