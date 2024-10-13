# from django.shortcuts import render
# from django.http import HttpResponse

# Here we create the route logic for the page app (app respective) (Ex: function based approach) XX 
# def homePageView(request):
    # return HttpResponse("Hello world!, Checking...")


# Rending the template with the generic template view with the class based approach

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'  # Adding template name here

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 

# After linking the template with the view need to update the URLS.py file to handle the rest 
