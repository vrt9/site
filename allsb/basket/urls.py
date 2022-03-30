from django.urls import path, base
from .views import *

urlpatterns = [

    path('', index, name='home'),
    # path('about/', about, name='home1'),
    path('base/', base, name='home2'),
]