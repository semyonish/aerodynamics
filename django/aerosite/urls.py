"""aerosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include

from django_registration.forms import RegistrationFormUniqueEmail
from aero_calculation.forms import MyRegistrationForm
from django_registration.backends.one_step.views import RegistrationView

from aero_calculation.forms import ProjectForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aero_calculation.urls')),
    path('accounts/register/',
        RegistrationView.as_view(form_class=MyRegistrationForm), {'form': RegistrationFormUniqueEmail},
        name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
]
