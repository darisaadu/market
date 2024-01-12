from django import forms
# from django.contrib.auth import get_user_model

INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl border'

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'User name',
        widget = forms.TextInput(attrs={
            'class': INPUT_CLASSES
        })
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'class': INPUT_CLASSES
        })
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label = 'User name',
        widget = forms.TextInput(attrs={
            'class': INPUT_CLASSES
        })
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'class': INPUT_CLASSES
        })
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'class': INPUT_CLASSES
        })
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'class': INPUT_CLASSES
        })
    )

