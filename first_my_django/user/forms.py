from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

data = None

def validated_password(value):
    global data
    if value:
        data = value
    data = value


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Password'
            }
        )
    )

    def is_login(self):
        login = authenticate(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password')
        )
        return login

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Username'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Email'
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Password'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'input',
                'placeholder': 'Confirm Password'
            }
        )
    )

    def clean_password(self):
        if data:
            raise forms.ValidationError("Password don't match")
        return self.cleaned_data.get('password')

    def clean(self):
        password = self.cleaned_data.get('password')
        if password != self.cleaned_data.get('confirm_password'):
            validated_password(True)
        user = User(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()