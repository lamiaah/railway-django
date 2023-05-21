from  django.urls import path
from convert.Api import views
urlpatterns = [

    path('', views.apirecord),
    
   
]
