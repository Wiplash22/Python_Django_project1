from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={
        'movies' : [
    {
        'title':'Inception',
        'name':'Christopher Nolan',
        'sucess': True
    },
    {
        'title':'Gravitiy',
        'name':'Christopher Nolan',
        'sucess': True
    },
    {
        'title':'Interstellar',
        'name':'Christopher Nolan',
        'sucess': True
    },
    {
        'title':'Tenet',
        'name':'Christopher Nolan',
        'sucess': False
    },
    {
        'title':'Avatar 3',
        'name':'James Cameron',
        'sucess': False
    },
    ]}
    return render(request, 'hello.html', movie_data)