"""
URL configuration for ram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from ram_rajya import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),   # Django admin panel
    path('',views.home), # your app urls
    path('owner',views.owner),
    path('cards/', views.cards_list, name='cards_list'),
    path('head-staff/', views.head_staff, name='head_staff'),
    path('artists/', views.artist_list, name='artist_list'),
    path('staff/', views.staff_list, name='staff_list'),
    path("free-fire/", views.free_fire , name="free_fire"),
    path('rules/', views.rules, name='rules'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
