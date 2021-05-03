from django.urls import path
from frontend.views import *


app_name = 'jobfrontend'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    # path('', home, name='home'),
]
