from django import forms
from .models import Patients
from .models import Doctors
from .models import Procedures



# create a patient input form
class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients  # which model(table) to be used in the form
        fields = ('firstname', 'lastname', 'hsnnum', 'ruhnum', 'dob', 'gender', 'location', 'status')  # which columns of the table being used
        labels = {   # use a blank label dictionary to cover the label of each fields
            'firstname': '',
            'lastname': '',
            'hsnnum': '',
            'ruhnum': '',
            'dob': '',
            'gender': '',
            'location': '',
            'status': '',
        }
        widgets = {  # use this to add bootstrap text input with placeholder
            'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'hsnnum': forms.TextInput(attrs={'class':'form-control', 'placeholder':'HSN'}),
            'ruhnum': forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUH Number'}),
            'dob': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Birth   yyyy-mm--dd'}),
            #'dob': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Birth', 'type':'date'}),  # using datepicker
            'gender': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gender'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'status': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Status'}),
        }


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors  # which model(table) to be used in the form
        fields = ('firstname', 'lastname')  # which columns of the table being used
        labels = {   # use a blank label dictionary to cover the label of each fields
            'firstname': '',
            'lastname': '',
        }
        widgets = {  # use this to add bootstrap text input with placeholder
            'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
        }


class ProceduresForm(forms.ModelForm):
    class Meta:
        model = Procedures  # which model(table) to be used in the form
        fields = ('proname', 'diagnosis', 'comments', 'admissiondate', 'xray', 'site', 'surgerydate', 'patient', 'doctor')  # which columns of the table being used
        labels = {   # use a blank label dictionary to cover the label of each fields
            'proname': '',
            'diagnosis': '',
            'comments': '',
            'admissiondate': '',
            'xray': '',
            'site': '',
            'surgerydate': '',
            'patient': 'Patient',
            'doctor': 'Doctor',
        }
        widgets = {  # use this to add bootstrap text input with placeholder
            'proname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Procedure Name'}),
            'diagnosis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Diagnosis'}),
            'comments': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Comments'}),
            'admissiondate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Admission Date  yyyy-mm-dd'}),
            'xray': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Xray'}),
            'site': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Site'}),
            'surgerydate': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Surgery Date  yyyy-mm-dd'}),
            'patient': forms.Select(attrs={'class':'form-select', 'placeholder':'Patient'}),
            'doctor': forms.Select(attrs={'class':'form-select', 'placeholder':'Doctor'}),
        }

