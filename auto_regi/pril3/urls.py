from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('',views.index),
    path('register',RegisterView.as_view)
]
