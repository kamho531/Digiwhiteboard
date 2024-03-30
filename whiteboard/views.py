from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView   # need this import for class-based view of list of patients
from django.views.generic.edit import DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Patients, Doctors, Procedures
from .forms import PatientsForm, DoctorsForm, ProceduresForm
from django.contrib import messages


# Create your views here.


class ProceduresDeleteView(LoginRequiredMixin, DeleteView):
    model = Procedures
    success_url = '/whiteboard/procedures' 
    template_name = 'procedures/proceduresdelete.html'
    login_url = "/login"   


class ProceduresUpdateView(LoginRequiredMixin, UpdateView):
    model = Procedures
    success_url = '/whiteboard/procedures'
    form_class = ProceduresForm
    template_name = 'procedures/proceduresform.html'
    login_url = "/login"


class ProceduresDetailView(LoginRequiredMixin, DetailView):
    model = Procedures
    context_object_name = 'procedures'
    template_name = 'procedures/proceduresdetail.html'
    login_url = "/login"


class ProceduresCreateView(LoginRequiredMixin, CreateView):
    model = Procedures
    success_url = '/whiteboard/procedures'
    form_class = ProceduresForm
    template_name = 'procedures/proceduresform.html'
    login_url = "/login"


class ProceduresListView(LoginRequiredMixin, ListView):   # class-based views for list of patients
    model = Procedures
    context_object_name = "procedures"
    template_name = 'procedures/procedureslist.html'
    login_url = "/login"


class DoctorsDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctors
    success_url = '/whiteboard/doctors' 
    template_name = 'doctors/doctorsdelete.html'
    login_url = "/login"   


class DoctorsUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctors
    success_url = '/whiteboard/doctors'
    form_class = DoctorsForm
    template_name = 'doctors/doctorsform.html'
    login_url = "/login"


class DoctorsCreateView(LoginRequiredMixin, CreateView):
    model = Doctors
    success_url = '/whiteboard/doctors'
    form_class = DoctorsForm
    template_name = 'doctors/doctorsform.html'
    login_url = "/login"


class DoctorsListView(LoginRequiredMixin, ListView):   # class-based views for list of doctors
    model = Doctors
    context_object_name = "doctors"
    template_name = 'doctors/doctorslist.html'
    login_url = "/login"



class PatientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Patients
    success_url = '/whiteboard/patients' 
    template_name = 'patients/patientsdelete.html'
    login_url = "/login"   


class PatientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Patients
    success_url = '/whiteboard/patients'
    form_class = PatientsForm
    template_name = 'patients/patientsform.html'
    login_url = "/login"


class PatientsDetailView(LoginRequiredMixin, DetailView):
    model = Patients
    context_object_name = 'patients'
    template_name = 'patients/patientsdetail.html'
    login_url = "/login"


class PatientsCreateView(LoginRequiredMixin, CreateView):
    model = Patients
    success_url = '/whiteboard/patients'
    form_class = PatientsForm
    template_name = 'patients/patientsform.html'
    login_url = "/login"


class PatientsListView(LoginRequiredMixin, ListView):   # class-based views for list of patients
    model = Patients
    context_object_name = "patients"
    template_name = 'patients/patientslist.html'
    login_url = "/login"


#class WhiteboardView(LoginRequiredMixin, TemplateView):   # not using class-based views due to not able to sync changes in model data to the whiteboard
    #patients = Patients.objects.all()
    #doctors = Doctors.objects.all()
    #procedures = Procedures.objects.all()
    #success_url = '/whiteboard'
    #template_name = 'whiteboard/whiteboard.html'
    #extra_context = {'patients': patients, 'doctors': doctors, 'procedures': procedures}
    #login_url = "/login" 


def whiteboard(request):   # use function-based view for display of whiteboard
    if request.user.is_authenticated:
        patients = Patients.objects.all()
        doctors = Doctors.objects.all()
        procedures = Procedures.objects.all()

        return render(request, 'whiteboard/whiteboard.html', 
                    {'patients': patients, 'doctors': doctors, 'procedures': procedures})    
    else:
        messages.success(request, "Must be logged in to view the whiteboard!")
        return redirect('login')
    

def searchpatient(request):
    if request.method == "POST":
        searched = request.POST['searched']
        patientsfn = Patients.objects.filter(firstname__contains=searched)
        patientsln = Patients.objects.filter(lastname__contains=searched)
        return render (request, 'patients/searchpatient.html',
                        {'searched':searched,
                         'patientsfn':patientsfn,
                         'patientsln':patientsln,})
    else:
        return render (request, 'patients/searchpatient.html',
                        {})


