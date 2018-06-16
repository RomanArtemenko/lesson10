from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShortlyForm
from .models import Shortly

# Create your views here.
def index(request):
    return render(request, 'shortly_app/index.html')
# "Top the most visited link"
    # return HttpResponse("Index, Hello World")

def catalog(request):
    shortly_list = Shortly.objects.all()
    return render(request, 'shortly_app/link_list.html', {'shortly_list':shortly_list})

def detail(request, shortly_id):
    return render(request, 'shortly_app/detail.html')
    # return HttpResponse("Detail, Hello World")

def new(request):
    form = ShortlyForm()
    if request.method == 'POST':
        form = ShortlyForm(request.POST)
        if form.is_valid():
            shortly = form.save()
            return redirect('detail', shortly_id=shortly.pk)
    return render(request, 'shortly_app/new.html', {'form':form})
    # return HttpResponse("New, Hello World")
