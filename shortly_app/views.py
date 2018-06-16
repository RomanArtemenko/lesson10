from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ShortlyForm
from .models import Shortly

# Create your views here.
def index(request):
    top5 = Shortly.objects.all().order_by('-visit_counter')[:5]
    return render(request, 'shortly_app/index.html', {'top5': top5})

def catalog(request):
    shortly_list = Shortly.objects.all()

    return render(request, 'shortly_app/link_list.html', {'shortly_list':shortly_list})

def detail(request, shortly_id):
    target = get_object_or_404(Shortly, pk=shortly_id)

    return render(request, 'shortly_app/detail.html', {'target':target})

def new(request):
    form = ShortlyForm()
    if request.method == 'POST':
        form = ShortlyForm(request.POST)
        if form.is_valid():
            shortly = form.save()
            return redirect('detail', shortly_id=shortly.pk)
    return render(request, 'shortly_app/new.html', {'form':form})

def follow_link(request, shortly_id):
    target = get_object_or_404(Shortly, pk=shortly_id)
    target.visit_counter += 1
    target.save()

    return redirect(target.link)