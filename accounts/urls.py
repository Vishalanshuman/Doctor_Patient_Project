from django.urls import path
from accounts import views


urlpatterns = [
    path('',views.home,name='home_page'),
    path('patient_signup/',views.PatientSignupView,name='patient_signup'),
    path('doctor_signup/',views.DoctorSignupView,name='doctor_signup'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),

]
