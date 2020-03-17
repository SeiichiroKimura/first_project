from django.views import generic
from .models import Category, Shop, Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BookForm
from django.views.generic import RedirectView

def index(request):
    context = {
    }
    return render(request, 'lunchmap/index.html', context)

def agenda(request):
    return render(request, 'lunchmap/agenda.html', context)

def venue(request):
    context = {
    }
    return render(request, 'lunchmap/venue.html', context)

def photolist(request):
    context = {
    }
    return render(request, 'lunchmap/photo_list.html', context)

def photo(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book()
            print(request)
            book.title = request.POST['title']
            book.link = request.POST['link']
            book.image = request.FILES['image']
            book.author = request.user
            book.save()
            return redirect('lunchmap: photolist', pk=book.pk)
    else:
        form = BookForm()
        obj = Book.objects.all()

    return render(request, 'lunchmap/photo.html', {
        'form': form,
        'obj': obj
        })

class DetailView(generic.DetailView):
    model = Book

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
