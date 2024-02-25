from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)
from app.models import AreaRecord, Profile
from django import forms


INPUT_CLASSES = """
    p-1 lg:p-2 border rounded-lg lg:w-full
"""

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = AreaRecord
        fields = [
            'month',
            'week',
            'area_name',
            'parish_name',
            'address',
            'area_coordinator', 
            'parish_number_with_report',
            'parish_number_with_no_report',
            'total_number_of_parish',
            ]
        widgets = {
            'month': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'week': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'area_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parish_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'area_coordinator': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parish_number_with_report': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parish_number_with_no_report': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'total_number_of_parish': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
        
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = AreaRecord
        fields = [
            'month',
            'week',
            'area_name',
            'parish_name',
            'address',
            'area_coordinator', 
            'parish_number_with_report',
            'parish_number_with_no_report',
            'total_number_of_parish',
            ]
        widgets = {
            'month': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'week': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'area_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parish_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'area_coordinator': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parish_number_with_report': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parish_number_with_no_report': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'total_number_of_parish': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'parish_name', 'parish_location',]
        
        
class PasswordForm(PasswordChangeForm):
    class meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']