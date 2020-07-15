from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Product


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    email= forms.EmailField(max_length=300, help_text='Required.Inform a valid Email')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
