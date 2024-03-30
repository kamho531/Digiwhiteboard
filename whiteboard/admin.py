from django.contrib import admin
from . import models


# Register your models here.
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')  

admin.site.register(models.Patients, PatientsAdmin)


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')

admin.site.register(models.Doctors, DoctorsAdmin)


class ProceduresAdmin(admin.ModelAdmin):
    list_display = ('proname', 'diagnosis', 'doctor')

admin.site.register(models.Procedures, ProceduresAdmin)

