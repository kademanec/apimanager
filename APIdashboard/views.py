# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import APIs

# Create your views here.


def index(request):
    APIdashboard = APIs.objects.all()[:50]
    context={
    'APIdashboard':APIdashboard
    }
    return render(request,'index.html',context)

def details(request,id):
    APIdashboard = APIs.objects.get(id=id)

    context={
    'APIdashboard':APIdashboard
    }
    return render(request,'details.html',context)
def add(request):
    if(request.method == 'POST'):
        print request.POST
        name = request.POST['name']
        link =request.POST['link']
        requesting = request.POST['requesting']
        APIdashboard = APIs(name=name, link=link, requesting=requesting)
        APIdashboard.save()

        return redirect('/apidashboard')

    else:
        return render(request,'partials/add.html')

def edit(request,id):
    print("id",id)
    APIdashboard=APIs.objects.get(pk=int(id))
    
    context={
    # 'todos':todos,
    'name':APIdashboard.name,
    'link':APIdashboard.link,
    'requesting':APIdashboard.requesting,
    }

    if(request.method == 'POST'):
        print request.POST
        APIdashboard.name = request.POST['name']
        APIdashboard.link =request.POST['link']
        APIdashboard.requesting =request.POST['requesting']

        APIdashboard.save()

        return redirect('/apidashboard')


    return render(request,'partials/edit.html',context)

def delete(request,id):
    print("id",id)
    APIdashboard = APIs.objects.get(pk=id).delete()
    return redirect('/apidashboard')
