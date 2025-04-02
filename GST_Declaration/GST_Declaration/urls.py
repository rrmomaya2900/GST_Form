"""
URL configuration for GST_Declaration project.

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
from django.urls import path
from GST_app import views
from GST_app.views import home, gst_form_view, submit_gst_form, success_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gst-form/', views.gst_form_view, name='gst_form'),
    path('api/submit-gst/', submit_gst_form, name='submit_gst_form'),
    path('success/', success_page, name='success_page'),
]
