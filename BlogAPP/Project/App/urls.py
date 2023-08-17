from django.urls import path
from . import views  

urlpatterns = [
    path("signup", views.Signup.as_view()),
    path("login", views.Login.as_view()),
    path("create", views.Create.as_view()),
    path("update", views.Update.as_view()),
]
