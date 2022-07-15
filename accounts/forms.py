from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import MentorDetails, StudentDetails, EntrepreneurDetails, Projects, InvestorDetails

# Student Form
class StudentForm(UserCreationForm):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(StudentForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user          

# Entrepreneur Form
class EntrepreneurForm(UserCreationForm):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(EntrepreneurForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Investor Form
class InvestorForm(UserCreationForm):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(InvestorForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  

# Mentor Form
class MentorForm(UserCreationForm):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(MentorForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  

# Student Details
class StudentFormDetails(forms.ModelForm):
    class Meta:                      
        model = StudentDetails        
        fields = ("photo","age","mobile","college","state","city","role","interest1", "interest2","interest3","about_yourself")

# Entrepreneur Details
class EntrepreneurFormDetails(forms.ModelForm):
    class Meta:                      
        model = EntrepreneurDetails        
        fields = ("photo","age","mobile","state","city","role","interest1", "interest2","interest3","about_yourself")

# Investor Details
class InvestorFormDetails(forms.ModelForm):
    class Meta:                      
        model = InvestorDetails       
        fields = ("mobile_number","landline_number","website","state","city","photo","about","focus_industries","focus_sectors","startup_stages","min_investment_range","max_investment_range")

# Mentor Details
class MentorFormDetails(forms.ModelForm):
    class Meta:                      
        model = MentorDetails      
        fields = ("mobile_number","website","state","city","photo","about","focus_industries","guidance_areas","startup_stages")

# Project Registrations
class ProjectsFormDetails(forms.ModelForm):
    class Meta:                      
        model = Projects        
        fields = "__all__"
 
