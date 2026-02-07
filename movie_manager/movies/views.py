from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
# Create your views here.

def create(request):
    if request.POST:
        frm=MovieForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm=MovieForm()
                
    return render(request, 'create.html', {'frm':frm})

def list(request):
    print(request.COOKIES)
    visits=int(request.COOKIES.get('visits',0))
    visits+=1
    movie_data = MovieInfo.objects.all()
    print(movie_data)
    response=render(request, 'list.html', {'movies': movie_data, 'visits': visits})
    response.set_cookie('visits', visits)
    return response

def edit(request,pk):
    instance_edit= MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST, instance=instance_edit)
        if frm.is_valid():
            instance_edit.save()
    else:
        frm=MovieForm(instance=instance_edit)
    return render(request, 'create.html', {'frm':frm})

def delete(request,pk):
    instance= MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_data = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies': movie_data})
