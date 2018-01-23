from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shop.models import Detail, DetailImage


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Необов'язково.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Необов'язково.")
    email = forms.EmailField(max_length=254, help_text="Обов'язково. Напишіть дійсну електронну адресу.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['car', 'detail', 'price', 'description',]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label="")
    class Meta:
        model = DetailImage
        fields = ('image',)
