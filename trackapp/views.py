from django.shortcuts import render
from .models import Tracks
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup


class Create(CreateView):
   template_name = 'home.html'
   model = Tracks
   fields = ('url', 'keywords')
   success_url = reverse_lazy('result')


def resultfunc(request):
   for post in Tracks.objects.all():
       url = post.url
       keywords = post.keywords
   list = []
   response = requests.get(url)
   bs = BeautifulSoup(response.text, "html.parser")
   ul_tag = bs.find_all(class_="topicsList_main")
   for tag in ul_tag[0]:
      title = tag.a.getText()
      url2 = tag.a.get("href")
      list.append([title, url2])
   context = {'list': list,}
   return render(request, 'list.html', context)