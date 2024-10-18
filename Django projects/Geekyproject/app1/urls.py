from app1 import views
from django.urls import path

urlpatterns=[

    path("lerndj/",views.Hello_Gautam),
    path("rj/",views.Hello_render),
    path('mr/',views.Main_render)
]