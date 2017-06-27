from django.shortcuts import render
from django.http import HttpResponse
from nltk.corpus import nps_chat
# Create your views here.

def index(request):
    posts = nps_chat.posts()
    return render(request,'index.html', {
        'posts': posts,
    })
