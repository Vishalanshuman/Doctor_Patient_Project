from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User,Address



class PatientSignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','profile_pic','username','email']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.is_patient=True
        if commit:
            user.save()
        return user

class DoctorSignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','profile_pic','username','email']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.is_doctor=True
        if commit:
            user.save()
        return user

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=['line1','city','state','pincode']
        exclude=('user',)
