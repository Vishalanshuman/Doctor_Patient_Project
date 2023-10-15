from django.shortcuts import render,redirect
from accounts.forms import PatientSignupForm,AddressForm,DoctorSignupForm,LoginForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate

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
            messages.success(request,"Patient Account Created Successfully.")
            return HttpResponseRedirect(reverse('home_page'))
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
            messages.success(request,"Doctor Account Created Successfully.")
            return HttpResponseRedirect(reverse('home_page'))
    context={'form':form,'form1':form1}
    return render(request,'doctorSignup.html',context)


def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.is_doctor:
                messages.success(request,"Login Successfully")
                return render(request,'doctorDashboard.html')
            else:
                messages.success(request,"Login Successfully.")
                return render(request,'patientDashboard.html')
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    messages.success(request,'Logout Successfully.')
    return redirect('home_page')
