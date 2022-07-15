from django.urls import path, include
from main import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('about/' , views.about , name = 'about'),
    path('startups/' , views.topStartUps , name = 'top-startups'),
    path('schemes/' , views.govtSchemes , name = 'schemes'),
    path('resources/' , views.reources , name = 'resources'), 
    path('predict' , views.prediction , name = 'prediction')
]