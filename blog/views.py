# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog_Detail
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
def home_view(request):
	obj=Blog_Detail.objects.all()
	return render(request,'home.html' ,{'items': obj})

def login(request):
	return render(request,'login.html',{})