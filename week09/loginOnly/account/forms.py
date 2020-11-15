# -*- coding:utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, forms
from django.core.validators import MinLengthValidator

length = 9


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        strip=True,
        min_length=9,
        max_length=63,
        validators=[MinLengthValidator(9)]
    )
    error_messages = {
        "min_length": f"Fields are required more and equal than {length}.",
        'invalid_login': "Invalid username or password",
        # 'inactive': "Inactive account"
    }
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(9)]
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        strip=True,
        min_length=9,
        max_length=63,
        validators=[MinLengthValidator(9)]
    )
    error_messages = {
        "min_length": f"Length is required more and equal than {length}",
        'password_mismatch': "Two passwords are not matched.",
    }
    password1 = forms.CharField(
        label="Password",
        max_length=128,
        min_length=9,
        strip=False,
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(9)],
    )
    password2 = forms.CharField(
        label="Password",
        max_length=128,
        min_length=9,
        strip=False,
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(9)],
    )
