from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user'}))