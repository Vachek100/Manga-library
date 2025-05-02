from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Manga


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class BorrowMangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['status', 'borrower']
        widgets = {
            'borrower': forms.HiddenInput(),
            'status': forms.HiddenInput(),
        }


class ReturnMangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['status']
        widgets = {
            'status': forms.HiddenInput(),
        }


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'status', 'cover']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)
