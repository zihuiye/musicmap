from django.shortcuts import render
from django.http import  HttpResponseRedirect,HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.conf.urls import url
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User

import json
# from django.core.serializers import serialize

from .models import mapmusic
# Create your views here.

def index(request):
	print(list(mapmusic.objects.values_list()))
	return render(request,'index.html')
def music(request):
	if request.method == 'POST':
		try:
			music = mapmusic.objects.create(musicid=request.POST["id"],
			lat=request.POST["lat"],lng=request.POST["lng"],
			uploaderemail=request.POST["uploaderemail"],text=request.POST["descript"])
		except Exception as e:
			print(e)
		print(request.POST)
		return HttpResponseRedirect(reverse('index'))
	elif request.method == 'GET':
		music = list(mapmusic.objects.all().values_list())
		return HttpResponse(json.dumps(music,cls=DjangoJSONEncoder))
def test(request):
	return render(request,'base.html')
