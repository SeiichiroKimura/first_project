from django.views import generic
from .models import Category, Shop
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
    }
    return render(request, 'lunchmap/index.html', context)

def agenda(request):
    context = {
        'message': 'Welcome my BBS',
        'players': ['勇者', '戦士', '魔法使い', '忍者']
    }
    return render(request, 'lunchmap/agenda.html', context)

def venue(request):
    context = {
    }
    return render(request, 'lunchmap/venue.html', context)

def photo(request):
    context = {
    }
    return render(request, 'lunchmap/photo.html', context)

class IndexView(generic.ListView):
    model = Shop

class DetailView(generic.DetailView):
    model = Shop

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Shop
    fields = ['name', 'address', 'category'] #'__all__'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Shop
    fields = ['name', 'address', 'category'] #'__all__'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('lunchmap:index')
