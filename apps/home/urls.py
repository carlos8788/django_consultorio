
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
