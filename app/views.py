from typing import Any
from django.shortcuts import render # type: ignore
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView,FormView
from app.forms import *
from app.models import *
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
        

# Rendering the page using the templateview class
class RenderHtmlTV(TemplateView):
    template_name = 'RenderHtmlTV.html'

    #sending the data from BE to FE in TemplateView
    # def get_context_data(self, **kwargs):
    #     ECDO = super().get_context_data(**kwargs)
    #     ECDO['name'] = 'Hareesh'
    #     ECDO['age'] = 21
    #     return ECDO
    
    
    # Sending the form from BE to FE 
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ECDO = super().get_context_data(**kwargs)
        ECDO['EVFO'] = VoterMF()
        return ECDO
    
    # After Post method activation
    def post(self,request):
        EVFDO = VoterMF(request.POST)
        if EVFDO.is_valid():
            EVFDO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid Data')

class RenderHtmlFV(FormView):
    template_name = 'RenderHtmlFV.html'
    form_class = VoterMF


    # This method will take a variable as form 
    # This method will check the POST method activation, Collecting the data from the
    # form and it will validate the collected data we just need to save the data
    # we need to provide the url mapping for this class view 
    def form_valid(self, form):
        form.save()
        return HttpResponse('Data inserted')
