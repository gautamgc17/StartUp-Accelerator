from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

class StudentDetails(models.Model):
    STATES_CHOICE = (
        ('Andaman and Nicobar', 'Andaman and Nicobar'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    )

    ROLES_CHOICE = (
        ('Student', 'Student'),
        ('Entrepreneur', 'Entrepreneur'),
        ('Mentor', 'Mentor'),
        ('Investor', 'Investor'),
        ('Organization', 'Organization')
    )

    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    college = models.CharField(max_length=200)
    state = models.CharField(max_length=100 , choices=STATES_CHOICE)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLES_CHOICE)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    about_yourself = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'StudentDetails'


class EntrepreneurDetails(models.Model):
    STATES_CHOICE = (
        ('Andaman and Nicobar', 'Andaman and Nicobar'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    )

    ROLES_CHOICE = (
        ('Student', 'Student'),
        ('Entrepreneur', 'Entrepreneur'),
        ('Mentor', 'Mentor'),
        ('Investor', 'Investor'),
        ('Organization', 'Organization')
    )

    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=100 , choices=STATES_CHOICE)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLES_CHOICE)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    about_yourself = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'EntrepreneurDetails'


class InvestorDetails(models.Model):

    STATES_CHOICE = (
        ('Andaman and Nicobar', 'Andaman and Nicobar'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    )

    THEMES_CHOICE = (
        ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'),
        ('SMART AUTOMATION', 'SMART AUTOMATION'),
        ('FITNESS & SPORTS', 'FITNESS & SPORTS'),
        ('HERITAGE & CULTURE', 'HERITAGE & CULTURE'),
        ('MEDTECH/BIOTECH/ HEALTHTECH', 'MEDTECH/BIOTECH/ HEALTHTECH'),
        ('SMART VEHICLES', 'SMART VEHICLES'),
        ('FINANCE', 'FINANCE'),
        ('ARICULTURE, FOODTECH & RURAL DEVELOPMENT', 'ARICULTURE, FOODTECH & RURAL DEVELOPMENT'),
        ('ROBOTICS AND DRONES', 'ROBOTICS AND DRONES'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('TOURISM', 'TOURISM'),
        ('CLEAN & GREEN TECHNOLOGY', 'CLEAN & GREEN TECHNOLOGY'),
        ('BLOCKCHAIN & CYBERSECURITY', 'BLOCKCHAIN & CYBERSECURITY'),
        ('RENEWABLE/ SUSTAINABLE ENERGY', 'ENEWABLE/ SUSTAINABLE ENERGY'),
        ('SMART EDUCATION', 'SMART EDUCATION'),
        ('DISASTER MANAGEMENT', 'DISASTER MANAGEMENT'),
        ('AERONAUTICS', 'AERONAUTICS'),
        ('MISCELLANEOUS', 'MISCELLANEOUS'),
    )

    STAGES_CHOICE = (
        ('Ideation', 'Ideation'),
        ('Validation', 'Validation'),
        ('EarlyTraction', 'EarlyTraction'),
        ('Scaling', 'Scaling'),
    )

    SECTORS_CHOICE = (
        ('Big Data', 'Big Data'),
        ('Business Intelligence', 'Business Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('NLP', 'NLP'),
        ('Bitcoin and Blockchain', 'Bitcoin and Blockchain'),
        ('Pharmaceutical', 'Pharmaceutical'),
        ('Digital Media Publishing', 'Digital Media Publishing'),
        ('Foreign Exchange', 'Foreign Exchange'),
        ('Food Processing', 'Food Processing'),
        ('Healthcare Services', 'Healthcare Services'),
        ('Virtual Games', 'Virtual Games'),
        ('Trading', 'Trading'),
        ('Augmented + Virtual Reality', 'Augmented + Virtual Reality'),
        ('Construction Technologies', 'Construction Technologies'),
        ('Smart Home', 'Smart Home'),
        ('Internet of Things', 'Internet of Things'),
        ('Crowdfunding', 'Crowdfunding'),
        ('P2P', 'P2P'),
        ('Finance', 'Finance'),
        ('E-commerce', 'E-commerce'),
        ('SAAS', 'SAAS'),
        ('Others', 'Others'),
    )
    
    mobile_number = models.CharField(max_length=12)
    landline_number = models.CharField(max_length=12, blank=True)
    website = models.URLField(blank = True, default = '')
    state = models.CharField(max_length=100 , choices=STATES_CHOICE)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    about = models.TextField()
    focus_industries = MultiSelectField(choices = THEMES_CHOICE)
    focus_sectors = MultiSelectField(choices = SECTORS_CHOICE)
    startup_stages = MultiSelectField(choices = STAGES_CHOICE)
    min_investment_range = models.IntegerField()
    max_investment_range = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'InvestorDetails'


class MentorDetails(models.Model):

    STATES_CHOICE = (
        ('Andaman and Nicobar', 'Andaman and Nicobar'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    )

    THEMES_CHOICE = (
        ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'),
        ('SMART AUTOMATION', 'SMART AUTOMATION'),
        ('FITNESS & SPORTS', 'FITNESS & SPORTS'),
        ('HERITAGE & CULTURE', 'HERITAGE & CULTURE'),
        ('MEDTECH/BIOTECH/ HEALTHTECH', 'MEDTECH/BIOTECH/ HEALTHTECH'),
        ('SMART VEHICLES', 'SMART VEHICLES'),
        ('FINANCE', 'FINANCE'),
        ('ARICULTURE, FOODTECH & RURAL DEVELOPMENT', 'ARICULTURE, FOODTECH & RURAL DEVELOPMENT'),
        ('ROBOTICS AND DRONES', 'ROBOTICS AND DRONES'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('TOURISM', 'TOURISM'),
        ('CLEAN & GREEN TECHNOLOGY', 'CLEAN & GREEN TECHNOLOGY'),
        ('BLOCKCHAIN & CYBERSECURITY', 'BLOCKCHAIN & CYBERSECURITY'),
        ('RENEWABLE/ SUSTAINABLE ENERGY', 'ENEWABLE/ SUSTAINABLE ENERGY'),
        ('SMART EDUCATION', 'SMART EDUCATION'),
        ('DISASTER MANAGEMENT', 'DISASTER MANAGEMENT'),
        ('AERONAUTICS', 'AERONAUTICS'),
        ('MISCELLANEOUS', 'MISCELLANEOUS'),
    )

    STAGES_CHOICE = (
        ('Ideation', 'Ideation'),
        ('Validation', 'Validation'),
        ('EarlyTraction', 'EarlyTraction'),
        ('Scaling', 'Scaling'),
    )

    SECTORS_CHOICE = (
        ('Big Data', 'Big Data'),
        ('Business Intelligence', 'Business Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('NLP', 'NLP'),
        ('Bitcoin and Blockchain', 'Bitcoin and Blockchain'),
        ('Pharmaceutical', 'Pharmaceutical'),
        ('Digital Media Publishing', 'Digital Media Publishing'),
        ('Foreign Exchange', 'Foreign Exchange'),
        ('Food Processing', 'Food Processing'),
        ('Healthcare Services', 'Healthcare Services'),
        ('Virtual Games', 'Virtual Games'),
        ('Trading', 'Trading'),
        ('Augmented + Virtual Reality', 'Augmented + Virtual Reality'),
        ('Construction Technologies', 'Construction Technologies'),
        ('Smart Home', 'Smart Home'),
        ('Internet of Things', 'Internet of Things'),
        ('Crowdfunding', 'Crowdfunding'),
        ('P2P', 'P2P'),
        ('Finance', 'Finance'),
        ('E-commerce', 'E-commerce'),
        ('SAAS', 'SAAS'),
        ('Others', 'Others'),
    )
    
    mobile_number = models.CharField(max_length=12)
    website = models.URLField(blank = True, default = '')
    state = models.CharField(max_length=100 , choices=STATES_CHOICE)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    about = models.TextField()
    focus_industries = MultiSelectField(choices = THEMES_CHOICE)
    guidance_areas = MultiSelectField(choices = SECTORS_CHOICE)
    startup_stages = MultiSelectField(choices = STAGES_CHOICE)
    startups_mentored = models.IntegerField(blank=True , default=0)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'MentorDetails'


class Projects(models.Model):
    THEMES_CHOICE = (
        ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'),
        ('SMART AUTOMATION', 'SMART AUTOMATION'),
        ('FITNESS & SPORTS', 'FITNESS & SPORTS'),
        ('HERITAGE & CULTURE', 'HERITAGE & CULTURE'),
        ('MEDTECH/BIOTECH/ HEALTHTECH', 'MEDTECH/BIOTECH/ HEALTHTECH'),
        ('SMART VEHICLES', 'SMART VEHICLES'),
        ('ARICULTURE, FOODTECH & RURAL DEVELOPMENT', 'ARICULTURE, FOODTECH & RURAL DEVELOPMENT'),
        ('ROBOTICS AND DRONES', 'ROBOTICS AND DRONES'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('TOURISM', 'TOURISM'),
        ('CLEAN & GREEN TECHNOLOGY', 'CLEAN & GREEN TECHNOLOGY'),
        ('BLOCKCHAIN & CYBERSECURITY', 'BLOCKCHAIN & CYBERSECURITY'),
        ('RENEWABLE/ SUSTAINABLE ENERGY', 'ENEWABLE/ SUSTAINABLE ENERGY'),
        ('SMART EDUCATION', 'SMART EDUCATION'),
        ('DISASTER MANAGEMENT', 'DISASTER MANAGEMENT'),
        ('AERONAUTICS', 'AERONAUTICS'),
        ('MISCELLANEOUS', 'MISCELLANEOUS'),
    )

    CATEGORY_CHOICE = (
        ('HARDWARE', 'HARDWARE'),
        ('SOFTWARE', 'SOFTWARE')
    )

    SECTOR_CHOICE = (
        ('Central Ministry', 'Central Ministry'),
        ('State Government', 'State Government'),
        ('Private', 'Private'),
        ('Cooperate', 'Cooperate'),
        ('NGO', 'NGO'),
        ('Semi-Government', 'Semi-Government'),
        ('PSU', 'PSU')
    )

    organization_name = models.CharField(max_length=200)
    sector = models.CharField(max_length=100 , choices = SECTOR_CHOICE)
    business_phone_number = models.CharField(max_length=15)
    document1 = models.FileField(upload_to = 'files/%Y/%m/%d/')
    document2 = models.FileField(upload_to = 'files/%Y/%m/%d/', blank = True)
    theme = models.CharField(max_length=100 , choices = THEMES_CHOICE)
    category = models.CharField(max_length=10 , choices = CATEGORY_CHOICE)
    problem_statement_title = models.TextField()
    problem_statement_description = models.TextField()
    demo_link = models.URLField(null = True, blank = True)
    dataset = models.URLField(null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.problem_statement_title








