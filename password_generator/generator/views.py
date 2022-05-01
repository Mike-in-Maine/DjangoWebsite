from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
import pandas as pd

def sj(request):
    return render(request, 'sj.html')

def sj_loaded(request):
    return render(request, 'sj_loaded.html')

def home(request):
    return render(request, 'home.html')

def dataframe(request):
    df = pd.read_csv("generator/april.csv")
    data_head = df#.iloc[0]
    print(data_head)
    mydict = {
        "df":data_head,
        "df_order_number": data_head['ABEPOID'],
        "df_fname": data_head['SHIPTONAME'],
        "df_country": data_head['SHIPTOCOUNTRY'],
        "df_email": data_head['BUYEREMAILADDRESS']
    }
    return render(request, 'data.html', context=mydict)
#{'head': data_head}

def password(request):
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
    return render(request, 'password.html', {'password':thepassword})

def about(request):
    return render(request, 'about.html')
def out(request):
    return render(request, 'exit.html')

#___Other functions____


#def table(request):
#    df = pd.read_csv("generator/templates/generator/april.csv")
#    # 'tableview/static/csv/20_Startups.csv' is the django
#    # directory where csv file exist.
#    # Manipulate DataFrame using to_html() function
#    geeks_object = df.to_html()
#    print(geeks_object)
#    myname = "Miky"

#    return HttpResponse(request, 'generator/password.html', {'table':geeks_object, 'name':myname})

#table('generatedpassword/')
