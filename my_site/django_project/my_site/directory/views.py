from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from directory.models import Author
from directory.models import Serie
from directory.models import Genre
from directory.models import Publisher
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class AuthorView(DetailView):
    model = Author
    #template_name = 'directory/templates/author_details.html'
    slug_url_kwarg = "not_slug"

class SerieView(DetailView):
    model = Serie
    slug_url_kwarg = "not_slug"

class GenreView(DetailView):
    model = Genre
    slug_url_kwarg = "not_slug"

class PublisherView(DetailView):
    model = Publisher
    slug_url_kwarg = "not_slug"

class AuthorList(ListView):
    model = Author
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(name__contains=data)
            return qs
        return qs
        #redirect = self.request.POST.get('detail')
        #if redirect:
        #    return reverse_lazy('author-create')

        
class SerieList(ListView):
    model = Serie
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(serie__contains=data)
            return qs
        return qs

class GenreList(ListView):
    model = Genre
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(genre__contains=data)
            return qs
        return qs

class PublisherList(ListView):
    model = Publisher
    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('key', None)
        if data != None:
            qs = qs.filter(pub__contains=data)
            return qs
        return qs

class CreateAuthor(CreateView):
    model = Author
    fields = ['name']
    def get_success_url(self):
        redirect = self.request.POST.get('detail')
        return reverse_lazy('author-detail-list')

class CreateSerie(CreateView):
    model = Serie
    fields = ['serie']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('serie-detail-list')

class CreateGenre(CreateView):
    model = Genre
    fields = ['genre']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('genre-detail-list')

class CreatePublisher(CreateView):
    model = Publisher
    fields = ['pub']
    def get_success_url(self):
        redirect = self.request.POST.get('author-detail-list')
        return reverse_lazy('publisher-detail-list')