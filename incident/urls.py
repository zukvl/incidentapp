"""incident URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from incidentapp import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:incident_id>/', views.incident_detail, name='incident-detail'),
    
    path('incidentapp/sign-in/', LoginView.as_view(template_name='incidentapp/sign_in.html'),
         name='incidentapp-sign-in'),
    
    path('incidentapp/sign-out/', LogoutView.as_view(next_page='/'),
         name='incidentapp-sign-out'),
    
    path('incidentapp/', views.incidentapp_home, name='incidentapp-home'),
    
    path('incidentapp/incident/add', views.incidentapp_add_incident, name='incidentapp-add-incident'),
    
    path('incidentapp/component/add', views.incidentapp_add_component, name='incidentapp-add-component'),
    
    path('incidentapp/component', views.incidentapp_component, name='incidentapp-component'),
    
    path('incidentapp/status', views.incidentapp_status, name='incidentapp-status'),
]
