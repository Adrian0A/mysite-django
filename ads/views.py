from django.shortcuts import render
from django.views.generic.edit import UpdateView
from ads.models import Ad
from ads.owner import OwnerCreateView,OwnerDeleteView,OwnerDetailView,OwnerListView,OwnerUpdateView

# Create your views here.

class AdDeleteView(OwnerDeleteView):
    model = Ad

class AdListView(OwnerListView):
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title','price','text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title','price','text']