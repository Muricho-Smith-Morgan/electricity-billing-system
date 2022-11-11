from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from .models import Complaint
from django.contrib import messages
from django.template import loader
from .forms import EditForm, UpdatecomplaintInfoForm
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate



# Create your views here.

def hello(request):
    return render(request, 'electricity/hello.html',)

def panel(request):
    return render(request, 'electricity/panel.html',)


def response(request):
    return render(request, 'electricity/response.html',)

# def complaint(request):
#     return render(request, 'electricity/complaint.html',)


def edit(request, pk):
    complaint = Complaint.objects.get(id=pk)
    form = EditForm(instance=complaint)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        

    context = {'edit_form': form}
    return render(request, 'electricity/edit.html', context)

def delete(request, pk):
    obj = Complaint.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, 'complaint details deleted successfully.')
        return redirect('admin_panel')

    context = {'obj': obj}
    return render(request, 'electricity/delete.html', context)

def admin_panel(request):
    mydata = Complaint.objects.all().values()
    context = {'mymembers': mydata}
    return render(request, 'electricity/admin_panel.html', context)


def lodge(request):
    if request.method == 'POST':
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        residence = request.POST['residence']
        problem = request.POST['problem']
        email = request.POST['email']
        phone_no = request.POST['phonenumber']

        complaint_info = Complaint.objects.create(first_name=f_name, last_name=l_name, residence=residence, problem=problem,  email=email, phone_number=phone_no)
        complaint_info.save()

        return redirect('response')
    
    
    return render(request, 'electricity/lodge.html')

def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username = Username, password = Password)

        if user is not None:
            auth.login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request, 'Invalid details')
            return redirect('login')
    
    return render(request, 'electricity/login.html')







def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            

            return redirect('customer_login')
    else:
        form = SignUpForm()
    
    return render(request, 'electricity/register.html', {'form': form})

def customer_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # login(request, user)
                return redirect("panel")
            else:
                messages.error(request, "user does not exist or wrong password")

    form = AuthenticationForm()

    return render(request, 'electricity/customer_login.html', context={"login_form": form})

