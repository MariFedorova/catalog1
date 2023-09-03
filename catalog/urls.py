from django.urls import path

from catalog import views
from catalog.views import home, contacts

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
