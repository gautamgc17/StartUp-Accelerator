from re import template
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required , permission_required
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from accounts.models import InvestorDetails, MentorDetails, Projects
from accounts.forms import StudentForm, StudentFormDetails, EntrepreneurForm, EntrepreneurFormDetails, ProjectsFormDetails, InvestorForm, InvestorFormDetails, MentorForm, MentorFormDetails


# Student Register
def studentRegister(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect('student-details')
        else:
            messages.error(request, "Unsuccessful Registration. Invalid Information.")
            return redirect('student-register')
    return render(request=request, template_name="accounts/studentRegister.html", context={'studentRegister_form':form})


# Entrepreneur Register 
def entrepreneurRegister(request):
    form = EntrepreneurForm()
    if request.method == "POST":
        form = EntrepreneurForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect('entrepreneur-details')
        else:
            messages.error(request, "Unsuccessful Registration. Invalid Information.")
            return redirect('entrepreneur-register')
    return render(request=request, template_name="accounts/entrepreneurRegister.html", context={'entrepreneurRegister_form':form})


# Investor Register
def investorRegister(request):
    form = InvestorForm()
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect('investor-details')
        else:
            messages.error(request, "Unsuccessful Registration. Invalid Information.")
            return redirect('investor-register')
    return render(request=request, template_name="accounts/investorRegister.html", context={'investorRegister_form':form})


# Mentor Register
def mentorRegister(request):
    form = MentorForm()
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect('mentor-details')
        else:
            messages.error(request, "Unsuccessful Registration. Invalid Information.")
            return redirect('mentor-register')
    return render(request=request, template_name="accounts/mentorRegister.html", context={'mentorRegister_form':form})


# Student Details
def studentDetails(request):
    studentform = StudentFormDetails()
    if request.method == 'POST':
        studentform = StudentFormDetails(request.POST , request.FILES)
        if studentform.is_valid():
            student = studentform.save(commit=False)
            student.user = request.user
            student.save()
            # logout(request)
            return redirect('dashboard')        # dashboard
        
    context = {
        "studentForm": studentform
    }
    return render(request , 'accounts/studentInfo.html' , context)


# Entrepreneur Details
def entrepreneurDetails(request):
    entrepreneurform = EntrepreneurFormDetails()
    if request.method == 'POST':
        entrepreneurform = EntrepreneurFormDetails(request.POST , request.FILES)
        if entrepreneurform.is_valid():
            entrepreneur = entrepreneurform.save(commit=False)
            entrepreneur.user = request.user
            entrepreneur.save()
            return redirect('dashboard')            # dashboard
        
    context = {
        "entrepreneurForm": entrepreneurform
    }
    return render(request , 'accounts/entrepreneurInfo.html' , context)


# Response
def registerResponse(request):
    return render(request , 'accounts/response.html')


# Investor Details
def investorDetails(request):
    investorform = InvestorFormDetails()
    if request.method == 'POST':
        investorform = InvestorFormDetails(request.POST , request.FILES)
        if investorform.is_valid():
            investor = investorform.save(commit=False)
            investor.user = request.user
            investor.save()
            logout(request)
            return redirect('successful-registration')       
        
    context = {
        "investorForm": investorform
    }
    return render(request , 'accounts/investorInfo.html' , context)


# Investor Single
def investor_single_details(request , pk):
    single_data = get_object_or_404(InvestorDetails , pk=pk)
    context = {
        'single_data': single_data,
    }
    print(dir(single_data))
    return render(request , 'accounts/investorForum.html' , context)


# Mentor Details
def mentorDetails(request):
    mentorform = MentorFormDetails()
    if request.method == 'POST':
        mentorform = MentorFormDetails(request.POST)
        if mentorform.is_valid():
            mentor = mentorform.save(commit=False)
            mentor.user = request.user
            mentor.save()
            logout(request)
            return redirect('successful-registration')       
        
    context = {
        "mentorForm": mentorform
    }
    return render(request , 'accounts/mentorInfo.html' , context)


# Logout
def logoutPage(request):
    logout(request)
    return redirect('/')

# Display dashboard
def dashboard(request):
    mentors = MentorDetails.objects.all()
    investors = InvestorDetails.objects.all()
    projects = Projects.objects.all()
    context = {
        'mentors': mentors,
        'investors': investors,
        'projects': projects,
    }
    return render(request , 'accounts/dashboard.html' , context)


# Student Login
def studentLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('dashboard')                      # dashboard
            else:
                messages.error(request,"Invalid username or password.")
                return redirect('student-login')
        else:
            messages.error(request,"Invalid username or password.")  
            return redirect('student-login')      
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/studentLogin.html", context={"studentLogin_form":form})


# Entrepreneur Login
def entrepreneurLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')                      # dashboard
            else:
                messages.error(request,"Invalid username or password.")
                return redirect('entrepreneur-login') 
        else:
            messages.error(request,"Invalid username or password.")
            return redirect('entrepreneur-login') 
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/entrepreneurLogin.html", context={"entrepreneurLogin_form":form})


# Projects Submission
def submitProjectIdea(request):
    projectform = ProjectsFormDetails()
    if request.method == 'POST':
        projectform = ProjectsFormDetails(request.POST, request.FILES)
        if projectform.is_valid():
            project = projectform.save()
            return redirect('successful-registration')          
    context = {
        'project_form':projectform
    }
    return render(request, "accounts/projectSubmit.html", context)


# user_name = request.user
# current_user = User.objects.get(username = user_name)
# print(current_user)
# first_name = current_user.first_name
# last_name = current_user.last_name
# userMail = current_user.email
# return 'done'


