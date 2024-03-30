from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))   
    first_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class':'form-control'}))  
    last_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class':'form-control'}))
    # must use email, first_name, last_name as they are predetermined by django i.e. firstname, lastname, Email won't save

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
