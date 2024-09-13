from django import forms
from django.contrib.auth.models import User as DjangoUser
from app.models import User as CustomUser

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Create and save the CustomUser
        custom_user = super().save(commit=False)
        custom_user.set_password(self.cleaned_data["password1"])
        
        if commit:
            custom_user.save()

        # Create and save the DjangoUser
        django_user = DjangoUser(username=custom_user.username, email=custom_user.email)
        django_user.set_password(self.cleaned_data["password1"])

        if commit:
            django_user.save()

        return custom_user