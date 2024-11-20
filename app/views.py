from django.shortcuts import render # type: ignore
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Returning the HttpResponse from functions
def Fbv_string(request):
    return HttpResponse('This is fbv')
# Returning the HttpResponse with class
class Cbv_string(View):
    def get(self,request):# This get object method is used to handle the request
        return HttpResponse('This is CBV')



#Returning the Html template from function
def Fbv_html(request):
    return render(request,'Fbv_html.html')

#Returning the Html template from class
class ClassBased(View):
    def get(self,request):
        return render(request,'ClassBased.html')
    
#inserting the data from FE to table using the functions

def insert_fbv(request):
    EVFO = VoterMF()
    if request.method == 'POST':
        VFDO = VoterMF(request.POST)
        if VFDO.is_valid():
            VFDO.save()
            return HttpResponse('Data is inserted')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_fbv.html',{'EVFO':EVFO})

#inserting the data from FE to table using the class

class InsertCbv(View):
    def get(self,request):
        EVFO = VoterMF()
        return render(request,'InsertCbv.html',{'EVFO':EVFO})
    def post(self,request):
        VFDO = VoterMF(request.POST)
        if VFDO.is_valid():
            VFDO.save()
            return HttpResponse('Data is inserted')
        else:
            return HttpResponse('Invalid data')