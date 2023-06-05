
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', view_public, name='obra_social'),
    # path('logout/', logout_view, name='logout'),
]
