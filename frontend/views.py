from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# from django.views.generic import TemplateView
from django.views import View
import requests

# Create your views here.


class HomeView(View):

    def get(self, request):
    
    	response = requests.get("https://nischay-herbal.herokuapp.com/job/view-all-job/")
    	jobdata = response.json()
    	# print(jobdata)
    	context = {'jobdata': jobdata}
    	return render(request, 'job/home.html', context)

class LoginView(View):

    def get(self, request):
        return render(request, 'job/login.html')        

