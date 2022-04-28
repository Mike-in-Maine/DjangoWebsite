from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
import pandas as pd


def table(request):
    df = pd.read_csv("generator/templates/generator/april.csv")
    # 'tableview/static/csv/20_Startups.csv' is the django
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    geeks_object = df.to_html()
    print(geeks_object)
    myname = "Miky"

    return HttpResponse(request, 'generator/password.html', {'table':geeks_object, 'name':myname})


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    df = pd.read_csv("generator/templates/generator/april.csv")
    # 'tableview/static/csv/20_Startups.csv' is the django
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    geeks_object = df.to_html()



    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    lenght = int(request.GET.get('lenght',12)) #default lenght 12
    thepassword = ''
    myname = "Miky"
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword, 'name':geeks_object})

def about(request):
    return render(request, 'generator/about.html')
def out(request):
    return render(request, 'generator/exit.html')

#table('generatedpassword/')
