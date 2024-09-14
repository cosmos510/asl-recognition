
from django import forms
from django.contrib.auth.models import User as DjangoUser
from app.models import User as CustomUser
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        # Create and save the CustomUser
        custom_user = super().save(commit=False)
        custom_user.set_password(self.cleaned_data["password"])
        
        if commit:
            custom_user.save()

        # Create and save the DjangoUser
        django_user = DjangoUser(username=custom_user.username, email=custom_user.email)
        django_user.set_password(self.cleaned_data["password"])

        if commit:
            django_user.save()

        return custom_user
    
from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
