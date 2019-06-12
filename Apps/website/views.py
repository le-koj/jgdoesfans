
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import HomePage, Poster, SocialMedia
from datetime import datetime

# Create your views here.
def home(request):
    contents = HomePage.objects.get()        # get homepage object version 1: index

    #___process slide show contents___#
    poster = Poster.objects.get()

    #___process social media contents___#
    #social_media = SocialMedia.objects.all()

    return render(request, 'index.html', {'page_content': contents,
                                          'image': poster
                                          })
