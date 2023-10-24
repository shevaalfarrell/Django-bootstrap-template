from django import forms

class RegisterForm(forms.Form):
    nama_category = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nama Category'}))