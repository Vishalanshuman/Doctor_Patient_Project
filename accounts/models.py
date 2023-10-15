from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# h. Address(line1, city, state, pincode)

class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    profile_pic=models.ImageField(upload_to="Profile_Pictures",null=True,blank=True)

class Address(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)
    line1=models.TextField()
    city= models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pincode=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.user_id.username


