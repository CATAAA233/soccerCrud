"""testU1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.index, name="index_view"),
    
    path('Estadios', views.stadiums, name="stadiums_view"),
    path('RegistrarEstadio', views.stadiumsRegister, name="stadiumsRegister_view"),
    path('EditarEstadio/<int:pk>', views.stadiumEdit, name="stadiumsEdit_view"),
    path('BorrarEstadio/<int:pk>', views.stadiumDelete, name="stadiumsDelete_view"),


    path('Equipos', views.teams, name="teams_view"),
    path('RegistrarEquipo', views.teamsRegister, name="teamsRegister_view"),
    path('EditarEquipo/<int:pk>', views.teamEdit, name="teamsEdit_view"),
    path('BorrarEquipo/<int:pk>', views.teamDelete, name="teamsDelete_view"),
    
    path('Jugadores', views.players, name="players_view"),
    path('RegistrarJugador', views.playersRegister, name="playersRegister_view"),
    path('EditarJugador/<int:pk>', views.playerEdit, name="palyerEdit_view"),
    path('BorrarJugador/<int:pk>', views.playerDelete, name="playerDelete_view"),


]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
