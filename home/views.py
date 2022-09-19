from ast import If
from copyreg import constructor
from http.client import REQUEST_ENTITY_TOO_LARGE
from mimetypes import init
from multiprocessing import context
import re
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages

from .forms import stadiumsRegisterForm, teamsRegisterForm
from .models import stadiumsModel, teamsModel
# Create your views here.


def index(request):

    cardOptions = [
        {
            "title": "Estadios",
            "imageSrc": "static/images/stadioAkron.jpg",
        },
        {
            "title": "Equipos",
            "imageSrc": "static/images/Teams.jpg",
        },
        {
            "title": "Jugadores",
            "imageSrc": "static/images/Jugadores.png",
        }
    ]
    context = {
        "cardItems": cardOptions,
    }
    return render(request, "pages/home/index.html", context)

#-------------------------------------------------------------------------------------------------
def stadiums(request):
    stadium = stadiumsModel.objects.all()
    print(stadium)
    
    context = {
        "cardItem": stadium
    }
    return render(request, "pages/stadiums/index.html", context)

def stadiumsRegister(request):
    form = stadiumsRegisterForm()
    context = {
        "form":form
    }
    if request.method == 'POST':
        print('POST DETECTADO')
        print(request.FILES)
        form = stadiumsRegisterForm(request.POST, files=request.FILES)
        print(form)
        if form.is_valid():
            print('FORM VALIDO')
            stadium = stadiumsModel()
            stadium.name = form.cleaned_data['name']
            stadium.location = form.cleaned_data['location']
            stadium.capacity = form.cleaned_data['capacity']
            stadium.image = form.cleaned_data['image']
            stadium.save();
            print('guardado')
            return redirect('/Estadios')
        else:
            context={
                "error":"Error al registrar"
            }

    return render(request, "pages/stadiumsRegister/index.html", context)

def stadiumEdit(request,pk):
    stadium = get_object_or_404(stadiumsModel,id=pk)

    print(stadium.image)
    initialData= {
        "name": stadium.name,
        "location":stadium.location,
        "capacity":stadium.capacity,
        "image":stadium.image
    }
    form= stadiumsRegisterForm(initialData)
    context={
        "form":form,
    }

    if request.method == 'POST':
        print(request.FILES)
        form = stadiumsRegisterForm(request.POST, files=request.FILES)

        if form.is_valid():
            print('FORM VALIDO')
            stadium.name = form.cleaned_data['name']
            stadium.location = form.cleaned_data['location']
            stadium.capacity = form.cleaned_data['capacity']
            stadium.image = form.cleaned_data['image']
            stadium.save();
            print('Actualizado')
        else:
            context={
                "error":"Error al actualizar"
            }
    return render(request,'pages/stadiumsEdit/index.html',context )

def stadiumDelete(request,pk):
    stadium = get_object_or_404(stadiumsModel,id=pk)
    if request.method == 'POST':
        print('se esta eliminando')
        stadium.delete()
        return redirect('/Estadios')
    return render(request,'pages/stadiumsDelete/index.html',{} )

#------------------------------------------------------------------------------------------------------
def teams(request):
    teamItems = teamsModel.objects.all()
    
    context = {
        "cardItem": teamItems
    }
    return render(request, 'pages/teams/index.html', context)


def teamsRegister(request):
    stadiums = stadiumsModel.objects.all()
    stadiumAvaibles =[]
    for stadium in stadiums:
        stadiumAvaibles.append(stadium.name)

    print(stadiumAvaibles)
    form = teamsRegisterForm()
    context = {
        "form":form,
        "stadiumsAvaible":stadiums
    }
    if request.method == 'POST':
        print('POST DETECTADO')
        print(request.FILES)
        form = teamsRegisterForm(request.POST, files=request.FILES)
        print(form.data['stadium'])
        if form.is_valid():
            stadiumObject = get_object_or_404(stadiumsModel, name=form.data['stadium'])
            team = teamsModel()
            team.name = form.cleaned_data['name']
            team.location = form.cleaned_data['location']
            team.stadium = stadiumObject
            team.nickname = form.cleaned_data['nickname']
            team.image = form.cleaned_data['image']
            team.save()
            print('guardado')
            return redirect('/Equipos')
        else:
            context={
                "error":"Error al registrar"
            }
    return render(request, 'pages/teamsRegister/index.html', context)

def teamEdit(request,pk):
    team = get_object_or_404(teamsModel,id=pk)
    stadiumAvaibles = stadiumsModel.objects.all()
    initialData= {
        "name": team.name,
        "location":team.location,
        "nickname":team.nickname,
        "image":team.image
    }
    form= teamsRegisterForm(initialData)
    context={
        "form":form,
        "stadiumsAvaible":stadiumAvaibles
    }

    if request.method == 'POST':
        print(request.FILES)
        form = teamsRegisterForm(request.POST, files=request.FILES)

        if form.is_valid():
            team.name = form.cleaned_data['name']
            team.location = form.cleaned_data['location']
            if team.stadium.name != form.cleaned_data['stadium']:
                stadiumObject = get_object_or_404(stadiumsModel, name=form.data['stadium'])
                team.stadium = stadiumObject
            team.nickname = form.cleaned_data['nickname']
            team.image = form.cleaned_data['image']
            team.save();
            return redirect('/Equipos')
        else:
            context={
                "error":"Error al actualizar"
            }
    return render(request,'pages/teamsEdit/index.html',context )

def teamDelete(request,pk):
    print(pk)
    team = get_object_or_404(teamsModel,id=pk)
    if request.method == 'POST':
        print('se esta eliminando')
        team.delete()
        return redirect('/Equipos')
    return render(request,'pages/teamsDelete/index.html',{} )

#--------------------------------------------------------------------------------------------
def players(request):
    playerItems = [
        {
            "name": "David de gea",
            "team": "MANCHESTER UNITED",
            "age": "28",
            "position": "Portero",
            "number": "7",
        },
        {
            "name": "David de gea",
            "team": "MANCHESTER UNITED",
            "age": "28",
            "position": "Portero",
            "number": "7",
        },
        {
            "name": "David de gea",
            "team": "MANCHESTER UNITED",
            "age": "28",
            "position": "Portero",
            "number": "7",
        },
    ]
    context = {
        "cardItem": playerItems
    }
    return render(request, 'pages/players/index.html', context)


def playersRegister(request):
    context = {

    }
    return render(request, 'pages/playersRegister/index.html', context)

def playerEdit(request):
    print('Se esta editando el equipo')
    return render(request,'pages/playersEdit/index.html',{} )

def playerDelete(request):
    print('Se esta Borrando el equipo')
    return render(request,'pages/playersDelete/index.html',{} )
