"""
URL configuration for foodmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from home import views as h_view

urlpatterns = [
    path('', h_view.home, name='home'),
    path('contact/',h_view.contact, name='contact'),
    path('user_sign/',h_view.user_sign, name='user_sign'),
    path('user_login/',h_view.user_login, name='user_login'),
    path('about/',h_view.about, name='about'),
    path('donation/',h_view.donation, name='donation'),
    path('thankyou/',h_view.thankyou, name='thankyou'),
    path('profile/',h_view.profile, name='profile'),
    path('ngo/',h_view.ngo, name='ngo'),
    path('dlist/',h_view.dlist, name= 'dlist'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)