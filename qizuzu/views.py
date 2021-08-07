from django.http import HttpResponse
from django.shortcuts import render

from lease.models import Category


def home(request):
    categories=Category.objects.all()
    return render(request,'home.html',{'categories':categories})