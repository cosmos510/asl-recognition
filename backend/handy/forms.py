from django import forms
from django.contrib.auth.models import User as DjangoUser
from app.models import User
from app.models import Feedback
import re


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError("Password must contain at least one letter.")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Password must contain at least one number.")
        if not re.search(r'[\W_]', password):
            raise forms.ValidationError("Password must contain at least one symbol.")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        custom_user = super().save(commit=False)
        custom_user.set_password(self.cleaned_data["password"])

        if commit:
            custom_user.save()
        django_user = DjangoUser(
            username=custom_user.username,
            email=custom_user.email)
        django_user.set_password(self.cleaned_data["password"])

        if commit:
            django_user.save()
        return custom_user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
