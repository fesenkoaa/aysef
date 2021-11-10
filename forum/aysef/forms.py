from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Support, Category, Article
from django.contrib.auth.models import User


class MessageForm(forms.ModelForm):

    number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'your whatsapp phone without "+"'}),
        label="Enter your phone:"
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),
        label="Enter your message:"
    )

    class Meta:
        model = Support
        fields = ('number', 'message')