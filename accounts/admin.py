from django.contrib import admin
from accounts.models import EntrepreneurDetails, InvestorDetails, MentorDetails, Projects, StudentDetails

# Register your models here
admin.site.register([
    StudentDetails,
    MentorDetails,
    EntrepreneurDetails,
    InvestorDetails,
    Projects,
])

