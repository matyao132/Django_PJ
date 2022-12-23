from django.urls import path
from . import views

app_name = 'generate_estimate'

urlpatterns = [
    path('',views.top,name='top'),
]
