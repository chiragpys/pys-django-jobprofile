from django.urls import path
from . import views

app_name = 'candidate'

urlpatterns = [
    path('form', views.CreateCandidateProfile.as_view(), name='form')
]