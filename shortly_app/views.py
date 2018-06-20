from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView
from .forms import ShortlyForm
from .models import Shortly

# Create your views here.
class TopView(ListView):
    context_object_name = 'top'
    queryset = Shortly.objects.top()
    template_name = 'shortly_app/index.html'

class LinksView(ListView):
    model = Shortly
    template_name = 'shortly_app/link_list.html'
    paginate_by = 7

class ShortlyView(View):
    
    def get(self, request, *args, **kwargs):
        shortly = get_object_or_404(Shortly, pk=kwargs['shortly_id'])
        shortly.update_counter()
        return redirect(shortly.link)
        

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