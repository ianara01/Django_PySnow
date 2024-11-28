"""
URL configuration for config project.

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

from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from . import views
#from django.views import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.HomeView.as_view(), name='index'),      #1
    path("cafe/", include("cafe.urls")),
    path("blog/", include("blog.urls")),   # 2 blog URL 설정
]
                                    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),  # 4 debug_toolbar URL 설정
    ] + urlpatterns
