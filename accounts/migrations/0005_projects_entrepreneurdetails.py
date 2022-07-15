# Generated by Django 4.0.3 on 2022-03-13 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_alter_studentdetails_about_yourself_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=200)),
                ('sector', models.CharField(choices=[('Central Ministry', 'Central Ministry'), ('State Government', 'State Government'), ('Private', 'Private'), ('Cooperate', 'Cooperate'), ('NGO', 'NGO'), ('Semi-Government', 'Semi-Government'), ('PSU', 'PSU')], max_length=100)),
                ('business_phone_number', models.CharField(max_length=15)),
                ('document1', models.FileField(upload_to='photos/%Y/%m/%d/')),
                ('document2', models.FileField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('theme', models.CharField(choices=[('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'), ('SMART AUTOMATION', 'SMART AUTOMATION'), ('FITNESS & SPORTS', 'FITNESS & SPORTS'), ('HERITAGE & CULTURE', 'HERITAGE & CULTURE'), ('MEDTECH/BIOTECH/ HEALTHTECH', 'MEDTECH/BIOTECH/ HEALTHTECH'), ('SMART VEHICLES', 'SMART VEHICLES'), ('ARICULTURE, FOODTECH & RURAL DEVELOPMENT', 'ARICULTURE, FOODTECH & RURAL DEVELOPMENT'), ('ROBOTICS AND DRONES', 'ROBOTICS AND DRONES'), ('TRANSPORTATION', 'TRANSPORTATION'), ('TOURISM', 'TOURISM'), ('CLEAN & GREEN TECHNOLOGY', 'CLEAN & GREEN TECHNOLOGY'), ('BLOCKCHAIN & CYBERSECURITY', 'BLOCKCHAIN & CYBERSECURITY'), ('RENEWABLE/ SUSTAINABLE ENERGY', 'ENEWABLE/ SUSTAINABLE ENERGY'), ('SMART EDUCATION', 'SMART EDUCATION'), ('DISASTER MANAGEMENT', 'DISASTER MANAGEMENT'), ('AERONAUTICS', 'AERONAUTICS'), ('MISCELLANEOUS', 'MISCELLANEOUS')], max_length=100)),
                ('category', models.CharField(choices=[('HARDWARE', 'HARDWARE'), ('SOFTWARE', 'SOFTWARE')], max_length=10)),
                ('problem_statement_title', models.TextField()),
                ('problem_statement_description', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('dataset', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='EntrepreneurDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=15)),
                ('state', models.CharField(choices=[('Andaman and Nicobar', 'Andaman and Nicobar'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Entrepreneur', 'Entrepreneur'), ('Mentor', 'Mentor'), ('Investor', 'Investor'), ('Organization', 'Organization')], max_length=50)),
                ('interest1', models.CharField(max_length=100)),
                ('interest2', models.CharField(max_length=100)),
                ('interest3', models.CharField(max_length=100)),
                ('about_yourself', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'StudentDetails',
            },
        ),
    ]
