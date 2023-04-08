from django.urls import path
from . import views
from .views import RegisterView,LoginViev,UserView


urlpatterns = [
    path('',views.index),
    path('register',RegisterView.as_view()),
    path('login', LoginViev.as_view()),
    path('user', UserView.as_view()),
]
