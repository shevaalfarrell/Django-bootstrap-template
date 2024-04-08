from django import forms
from .models import Blog
from datetime import datetime
from django.contrib.auth.models import User

class Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category','detail','description','file']
        widgets = {
            'category' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'detail' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'detail'}),
            'description' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        instance.tanggal_dibuat = datetime.now()
        instance.tanggal_diperbarui = datetime.now()
        instance.author = self.user
        if commit:
            instance.save()
        return instance

class EditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category','detail','description', 'file']
        widgets = {
            'category' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'detail' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'detail'}),
            'description' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }
    def save(self, commit=True):
        instance = super(EditForm, self).save(commit=False)
        instance.tanggal_diperbarui = datetime.now()
        instance.author = self.user
        if commit:
            instance.save()
        return instance