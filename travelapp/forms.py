from django import forms
from travelapp.models import People
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddPeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

class UpdatePeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

        labels ={
            'name' : "Updated Name",
            'age' : "Updated Age",
            'address' : "Updated Address",
            'phone_no' : "Updated Phone No"
            }        
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']