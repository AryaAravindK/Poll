from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_poll, name='select_poll'),
    
    # Other URL patterns
]
