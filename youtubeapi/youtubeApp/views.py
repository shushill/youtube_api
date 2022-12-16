from django.shortcuts import render
from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
#from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .serializers import *

# Rest FrameWork
from rest_framework import generics
from django.db.models import Q


from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getvideo(request):
    video = VideoDetail.objects.all()
    serializer = VideosSerializer(video, many=True)
    return Response(serializer.data)


# Create your views here.
def home(request):
    if request.method == 'GET':
        q = request.GET.get('query')
        if q:
            res = VideoDetail.objects.filter(Q(video_title=q)| Q(video_desc=q))
            page = request.GET.get('page', 1)
            paginator = Paginator(res, 10)
            try:
                res = paginator.page(page)
            except PageNotAnInteger:
                res = paginator.page(1)
            except EmptyPage:
                res = paginator.page(paginator.num_pages)
            context = {'videolist': res}
            return render(request, 'index.html', context)
        else:
            res = VideoDetail.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(res, 10)
            try:
                res = paginator.page(page)
            except PageNotAnInteger:
                res = paginator.page(1)
            except EmptyPage:
                res = paginator.page(paginator.num_pages)
            context = {'videolist': res}
            return render(request, 'index.html', context)


