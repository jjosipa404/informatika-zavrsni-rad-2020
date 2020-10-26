from django.shortcuts import render
from . import services
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (

    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView

)
import pandas as pd
from .models import Comment, Post

# Create your views here.
def home(requests):
    return render(requests, 'corona/index.html')

def index(requests):
    summary_global = services.get_summary()["Global"]  #--  RADI --
    summary_countries = services.get_summary()["Countries"]  #--  RADI --

    return render(requests, 'corona/index.html',context={'summary_global':summary_global,'summary_countries':summary_countries})

def world(requests):
    return render(requests, 'corona/world.html')


def travel(requests):
    data = services.get_travel_data()
    return render(requests,'corona/travel.html', context={'data':data})

def countries(requests):
    data = services.by_countries_data()
    return render(requests,'corona/countries.html', context={'data':data})

 
# --- CREATE ---
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content','country']
    template_name = 'corona/post_create.html'
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'corona/comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

# --- READ ---
class PostDetailView(DetailView):
    model = Post


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        countryName = post.get_country_display()
        countryCode = post.country
        travel_news = services.get_travel_data()["data"]  #--  RADI --
        cnews = services.country_data(countryCode)["data"][0]

        tnews = ''
        for n in travel_news:
            if(n["location"] == countryName):
                tnews = n["data"]

        context['travel_news'] = tnews  #--  RADI --
        context['cases_news'] = cnews  #--  RADI --
        context['code'] = countryCode  #--  RADI --


        df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTxATUFm0tR6Vqq-UAOuqQ-BoQDvYYEe-BmJ20s50yBKDHEifGofP2P1LJ4jWFIu0Pb_4kRhQeyhHmn/pub?gid=0&single=true&output=csv')
        df = df.loc[df["adm0_name"] == countryName]
        data=pd.DataFrame({
            'adm0_name' : list(df["adm0_name"]),
            'iso3':list(df["iso3"]),
            'X':list(df["X"]),
            'Y':list(df["Y"]),
            'published':list(df["published"]),
            'sources':list(df["sources"]),
            'info':list(df["info"]),
            'optional1':list(df["optional1"]),
            'optional2':list(df["optional2"]),
            'optional3':list(df["optional3"]),
            'ObjectId':list(df["ObjectId"]),
        })
      
        context["travel_quarantine"] = data["optional2"][0]
        context["travel_certificate"] = data["optional3"][0]

        return context

class PostListView(ListView):
    model = Post
    template_name = 'corona/forum.html'  
    context_object_name = 'posts'
    ordering = ['-dateCreated']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# --- UPDATE ---
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'country']
    template_name = 'corona/post_update.html'  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'corona/comment_update.html'  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

# --- DELETE ---
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'
    template_name = 'corona/post_confirm_delete.html'  


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/posts'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user or self.request.user == comment.post.autor:
            return True
        return False


