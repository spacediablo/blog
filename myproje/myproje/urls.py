"""
URL configuration for myproje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, re_path, path
from django.contrib.auth.views import LoginView, LogoutView
from blog import views
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),
    re_path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    #re_path(r'^accounts/login/$',LoginView.as_view(), name='login'),
    #r#e_path(r'^accounts/logout/$', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
