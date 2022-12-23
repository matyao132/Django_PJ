from django.urls import path
from .views import Index

app_name = 'macyao_blog'

urlpatterns = [
    path('',Index.as_view(),name='index'),
]
