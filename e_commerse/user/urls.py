from django.urls import path
from .views import *
app_name = "user"

urlpatterns = [
    #path('user/', views.userlist, name='user'),
    path('signup/', sign_up, name='sign_up'),
    path('signin/', sign_in, name='sign_in'),
    path('signout/', sign_out, name='sign_out'),
]