"""
URL configuration for Geekyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from  app1 import views as ap1
# from app2 import views as ap2
# from app1.views import Hello_Gautam
# from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('learndj/',ap2.learn_django),
    # path('dj1/',ap2.learn_html),
    # path('dj2/',ap2.learn_djhtml),
    # path('dj3/',ap2.learn_variable),
    # path('Gt/',Hello_Gautam)
    path('dt/',include('app1.urls')),
    path('dm/',include('app2.urls'))
]
