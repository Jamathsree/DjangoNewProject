from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView

from .forms import ServiceForm, WorkerForm, LoginForm, CustomerForm, Worker_scheduleForm,AppointmentForm,ComplaintForm
from .models import Services, Worker, Customer, Worker_schedule, Login,Appoinment,Complaint


#################################ADMIN DASHBOARD########################
def Home(request):
    return render(request, 'Homepage.html')

@login_required(login_url='login_view')
def admin_home(request):
    return render(request, 'admintemp/index.html')


@login_required(login_url='login_view')
def add_services(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'admintemp/Services.html', {'form': form})


@login_required(login_url='login_view')
def service_view(request):
    obj = Services.objects.all()
    return render(request, 'admintemp/service_view.html', {'obj': obj})


@login_required(login_url='login_view')
def service_delete(request, id):
    form = Services.objects.get(id=id)
    form.delete()
    return redirect("service_view")
def worker_register(request):
    worker_form = WorkerForm()
    login_form = LoginForm()
    if request.method == 'POST':
        worker_form = WorkerForm(request.POST, request.FILES)
        login_form = LoginForm(request.POST)
        if worker_form.is_valid() and login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_Worker = True
            user.save()
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            return redirect('login_view')
    return render(request, 'admintemp/Worker_register.html', {'worker_form': worker_form, 'login_form': login_form})

@login_required(login_url='login_view')
def Worker_view(request):
    obj = Worker.objects.all()
    return render(request, 'admintemp/Worker_view.html', {'obj': obj})


@login_required(login_url='login_view')
def Worker_edit_views(request, id):
    obj = Worker.objects.get(id=id)
    form = WorkerForm(instance=obj)
    if request.method == 'POST':
        form = WorkerForm(request.POST or None, instance=obj)
        form.save()
    return render(request, 'admintemp/Worker_edit_views.html', {'form': form})


@login_required(login_url='login_view')
def Worker_delete_views(request, id):
    form = Worker.objects.get(id=id)
    form.delete()
    return redirect("Worker_view")


@login_required(login_url='login_view')
def Customer_view(request):
    obj = Customer.objects.all()
    return render(request, 'admintemp/Customer_view.html', {'obj': obj})


@login_required(login_url='login_view')
def Customer_edit_views(request, id):
    obj = Customer.objects.get(id=id)
    form = CustomerForm(instance=obj)
    if request.method == 'POST':
        form = CustomerForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()

    return render(request, 'admintemp/Customer_edit_view.html', {'form': form})


@login_required(login_url='login_view')
def Customer_delete_views(request, id):
    form = Customer.objects.get(id=id)
    form.delete()
    return redirect("Customer_view")


##############################################ADMIN DASHBOARD ENDS##########
@login_required(login_url='login_view')
def Schedule_add(request):
    form = Worker_scheduleForm()
    if request.method == 'POST':
        form = Worker_scheduleForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=Worker.objects.get(user=request.user)
            form.save()
            return redirect('Worker_home')
    return render(request, 'Workertemp/Schedule_add.html', {'form': form})


@login_required(login_url='login_view')
def Worker_schedule_view(request):  # don't  give same name of function  in the object
    data= Worker.objects.get(user=request.user)
    obj = Worker_schedule.objects.filter(user=data)
    return render(request, 'Workertemp/Worker_schedule_view.html', {'obj': obj})


@login_required(login_url='login_view')
def Worker_schedule_edit(request, id):
    obj = Worker_schedule.objects.get(id=id)
    form = Worker_scheduleForm(instance=obj)
    if request.method == 'POST':
        form = Worker_scheduleForm(request.POST or None, instance=obj)
        form.save()
    return render(request, "Workertemp/Worker_schedule_edit.html", {'form': form})



@login_required(login_url='login_view')
def Worker_schedule_delete(request, id):
    form = Worker_schedule.objects.get(id=id)
    form.delete()
    return redirect('Worker_schedule_view')

def register(request):
    form = LoginForm
    return render(request, "register.html", {"form": form})


# Worker view starts


# Customer view starts
def Customer_register(request):
    customer_form = CustomerForm()
    login_form = LoginForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES)
        login_form = LoginForm(request.POST)
        if customer_form.is_valid() and login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_Customer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login_view')
    return render(request, 'customertemp/Customer_register.html', {'customer_form': customer_form, 'login_form': login_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_Worker:
                return redirect('Worker_home')
            elif user.is_Customer:
                return redirect('Customer_home')
            else:
                messages.info(request, "INVALID CREDENTIALS")
    return render(request, 'login.html')

@login_required(login_url='login_view')
def Customer_home(request):
    return render(request,'customertemp/Customer_home.html')
@login_required(login_url='login_view')
def Customer_profile(request):
    u=request.user
    obj=Login.objects.get(username=u)
    data=Customer.objects.filter(user=obj)
    print(data)
    return render(request,'customertemp/Customer_profile_view.html',{'data':data})

###########################Worker Dashboard############################################
@login_required(login_url='login_view')
def Worker_home(request):
    return render(request, 'Workertemp/Worker_home.html')

@login_required(login_url='login_view')
def Profile(request):
    u=request.user
    obj=Login.objects.get(username=u)
    data=Worker.objects.filter(user=obj)
    print(data)
    return render(request,'Workertemp/Worker_profile_view.html',{'data':data})

@login_required(login_url='login_view')
def Customer_schedule_view(request):
    obj = Worker_schedule.objects.all()
    return render(request,'customertemp/Customer_schedule_view.html',{'obj':obj})


#################### Customer ordered #############################

# Appoinment

@login_required(login_url='login_view')
def take_appointment(request,id):
    schedule = Worker_schedule.objects.get(id=id)
    u= Customer.objects.get(user=request.user)
    appointment = Appoinment.objects.filter(user=u,Worker_schedule=schedule)
    if appointment.exists():
        messages.info(request,'You Have Already Requested Appointment for this Schedule')
        return redirect('Customer_schedule_view')
    else:
        if request.method == 'POST':
            obj = Appoinment()
            obj.user = u
            obj.Worker_schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('view_appointment_user')
    return render(request,'customertemp/take_appointment.html',{'schedule': schedule})


@login_required(login_url='login_view')
def view_appointment_user(request):
    u = Customer.objects.get(user=request.user)
    appoinment = Appoinment.objects.filter(user=u)
    return render(request, 'customertemp/view_appointment.html', {'appointment':appoinment})

@login_required(login_url='login_view')
def view_appointment_worker(request):
    appoinment = Appoinment.objects.all()
    return render(request, 'Workertemp/Worker_appointment.html', {'appointment': appoinment})

@login_required(login_url='login_view')
def accept(request, id):
    appoinment = Appoinment.objects.get(id=id)
    appoinment.status =1
    appoinment.save()
    return redirect('view_appointment_user')

@login_required(login_url='login_view')
def reject (request, id):
    appoinment = Appoinment.objects.get(id=id)
    if request.method== 'POST':
        appoinment.status = 2
        appoinment.save()
        return redirect('view_appointment_user')
    return render(request,'Workertemp/reject_appoinment.html')

@login_required(login_url='login_view')
def Complaints(request):
    form = ComplaintForm()
    user=request.user
    print(user)
    if request.method == 'POST':
        form =ComplaintForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user = user
            obj.save()
    return render(request, 'customertemp/complaint.html', {'form':form})

@login_required(login_url='login_view')
def View_complaint(request):
    obj= Complaint.objects.all()
    return render(request, 'admintemp/View_complaint.html', {'obj': obj})

@login_required(login_url='login_view')
def reply_complaint(request,id):
    feedback= Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply =r
        feedback.save()
        messages.info(request,'Reply Send Sucessfully')
        return redirect('View_complaint')
    return render(request, 'admintemp/reply_complaint.html', {'feedback':feedback})

@login_required(login_url='login_view')
def View_reply(request):
    obj = Complaint.objects.all()
    return render(request, 'customertemp/reply_view.html', {'obj': obj})


def logout_view(request):
    logout(request)
    return redirect('login_view')



