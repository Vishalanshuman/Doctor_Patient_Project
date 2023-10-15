from django.shortcuts import render
from accounts.forms import PatientSignupForm,AddressForm,DoctorSignupForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'base.html')

def PatientSignupView(request):
    form=PatientSignupForm()
    form1=AddressForm()
    if request.method=="POST":
        form=PatientSignupForm(request.POST,request.FILES)
        form1=AddressForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user1=form.save()
            address=form1.save(commit=False)
            address.user_id=user1
            address.save()
            return HttpResponse("Form saved")
        return HttpResponse(form1.errors ,form.errors)
    context={'form':form,'form1':form1}
    return render(request,'patientSignup.html',context)


def DoctorSignupView(request):
    form=DoctorSignupForm()
    form1=AddressForm()
    if request.method=="POST":
        form=DoctorSignupForm(request.POST,request.FILES)
        form1=AddressForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user1=form.save()
            address=form1.save(commit=False)
            address.user_id=user1
            address.save()
            return HttpResponse("Form saved")
        return HttpResponse(form1.errors ,form.errors)
    context={'form':form,'form1':form1}
    return render(request,'patientSignup.html',context)
