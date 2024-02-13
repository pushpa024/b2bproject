from django.urls import path
from . import views

urlpatterns = [
    path('basic/', views.BasicContactView.as_view(), name='basic_contact'),
]
