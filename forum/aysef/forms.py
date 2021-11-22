from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms
from django.core.exceptions import ValidationError
from .models import EmailMessage, Category, Article
from django.contrib.auth.models import User


class MessageForm(forms.ModelForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}),
        label="Email"
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),
        label="Message"
    )

    class Meta:
        model = EmailMessage
        fields = ('email', 'message')


class AddArticleFrom(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('auth', 'category', 'title', 'text')
        widgets = {
            'auth': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('auth', 'category', 'title', 'text')
        widgets = {
            'auth': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),

        }


class RegForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
        label='Enter username:'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        label='Enter your email:'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        label='Enter your password:'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        label='Repeat your password:'
    )

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username'}),
        label='Username:')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'old password'}),
        label='Enter old password:')


class ResetPasswordForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}),
        label="Email"
    )

    class Meta:
        model = EmailMessage
        fields = ('email',)