from django.urls import path
from app2.views import *

app_name="app2"

urlpatterns=[
    path('mi/',mi,name='mi'),
    path('rohit/',rohit,name='rohit'),
]