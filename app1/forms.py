import datetime

from django import forms

from app1.models import Services, Login,Appoinment
from app1.models import Worker,Customer,Worker_schedule,Complaint
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ServiceForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=('name',)
class WorkerForm(forms.ModelForm):
     class Meta:
        model = Worker
        fields = ('name','address','phone_number','location','image')



class TimeInput(forms.TimeInput):
    input_type ='Time'

class DateInput(forms.DateInput):
    input_type='Date'
class Worker_scheduleForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    start_time=forms.TimeField(widget=TimeInput,)
    end_time = forms.TimeField(widget=TimeInput, )
    class Meta:
        model = Worker_schedule
        fields = ('start_time','end_time','date')



class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2')


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','address','phone_number','location')


# # class NewUserForm(UserCreationForm):
# #     class Meta:
# #         model = User
# #         fields = ("username", "password1", "password2")
# def save(self, commit=True):
#     user = super(NewUserForm, self).save(commit=False)
#     if commit:
#         user.save()
#     return user
class DateInput(forms.DateInput):
    input_type='Date'
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = '__all__'
        exclude=("status","user")

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ("content",)

# class ReplyForm(forms.Form):
#     rely = forms.CharField(widget=forms.Textarea,required=True)
#
#     def clean_reply(self):
#         reply = self.cleaned_data['reply']
#         if reply == '':
#             raise forms.ValidationError('This Filed is required')
#         return reply
