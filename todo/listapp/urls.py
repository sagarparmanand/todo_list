from django.urls import path,include
from listapp import views
from listapp.views import Home

urlpatterns = [
    path('',Home.as_view()),
    path('comp/<cid>',views.Iscomp.as_view()),
    path('delete/<did>',views.Delete.as_view()),
    path('sort/<sid>',views.Sort.as_view()),
   
]
