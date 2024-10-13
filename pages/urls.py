from django.urls import path
from.views import HomePageView, AboutPageView

# Need to make a route for the each new vew we create for each new endpoint 
urlpatterns = [
    # path('', homePageView, name='home'), Will do this if there is not template view involved 
    # new route should on top 
    path('about/', AboutPageView.as_view(), name='about'), # Will do this if there is template view involved  
    path('', HomePageView.as_view(), name='home'), # Will do this if there is template view involved 
]