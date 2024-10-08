"""media_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
    3. Test 1
    4. Test 2
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/video/', include(('video.urls', 'video'), namespace='v1:video')),
    path('user/', include('users.urls')),
    path('v1/auth/', include(('auth.urls', 'auth'), namespace='v1:auth')),
    path('v2/auth/', include(('auth.urls', 'auth'), namespace='v2:auth')),
    path('v1/services/', include(('services.urls', 'services'), namespace='v1:services'))
]
