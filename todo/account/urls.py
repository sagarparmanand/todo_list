from django.urls import path,include
# from account.views import Home
from account import views

urlpatterns = [
    path('login',views.Login.as_view()),
    path('register',views.Register.as_view()),
    path('logout',views.Logout.as_view()),
]