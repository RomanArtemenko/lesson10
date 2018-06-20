from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView
from .forms import ShortlyForm
from .models import Shortly

# Create your views here.
def index(request):
    top5 = Shortly.top5.all()

    return render(request, 'shortly_app/index.html', {'top5': top5})

class LinksView(ListView):
    model = Shortly
    template_name = 'shortly_app/link_list.html'

def follow_link(request, shortly_id):
    target = get_object_or_404(Shortly, pk=shortly_id)
    target.update_counter()

    return redirect(target.link)

class DetailView(TemplateView):
    template_name = 'shortly_app/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target'] = get_object_or_404(Shortly, pk=kwargs['shortly_id'])

        return context

class NewView(View):
    form_class = ShortlyForm
    template_name = 'shortly_app/new.html'

    def get(self, request, *args, **kwargs):
        form = ShortlyForm() 

        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            shortly = form.save()
            return redirect('detail', shortly_id=shortly.pk)

        return render(request, self.template_name, {'form':form})