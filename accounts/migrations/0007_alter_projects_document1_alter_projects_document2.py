# Generated by Django 4.0.3 on 2022-03-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_organization_projects_organization_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='document1',
            field=models.FileField(upload_to='files/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='document2',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/'),
        ),
    ]
