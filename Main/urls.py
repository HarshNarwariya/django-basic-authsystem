from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('index/', view=views.index, name="index")
]