from django.urls import path
from . import views

urlpatterns = [

    path("",views.index),
    path("hello/<str:usuario>",views.hello),
    path("create_task/",views.create_task),
]