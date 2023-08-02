from django.urls import path,include
from . import views

app_name = "spamdetect"

urlpatterns = [
    path('',views.home,name="home")
]
