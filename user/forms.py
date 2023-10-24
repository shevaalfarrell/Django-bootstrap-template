from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username'}))
    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Repeat Password'}))