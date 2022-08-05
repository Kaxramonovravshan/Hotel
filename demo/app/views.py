from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Feedback


def index(request):
    return render(request, 'pages/index.html')


def watch(request):
    return render(request, 'pages/watchfilm.html')

def feedback(request):
    if request.method=='POST':
        feedback = Feedback()
        name = request.POST.get('name')
        number = request.POST.get('number')
        number_person = request.POST.get('number_person')
        number_children = request.POST.get('number_children')
        select = request.POST.get('select')
        # return HttpResponse(select)
        feedback.name = name
        feedback.number = number
        feedback.number_person = number_person
        feedback.number_children = number_children
        feedback.select = select
        feedback.save()
    return render(request,'pages/finished.html')

