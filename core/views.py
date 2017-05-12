from django.shortcuts import render
from django.http import  HttpResponseRedirect,HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.conf.urls import url
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.utils import timezone
import pytz


import json
# from django.core.serializers import serialize

from .models import mapmusic
# Create your views here.

def index(request):
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
		timezone.activate(pytz.timezone("Asia/Shanghai"))
		music = list(mapmusic.objects.all().values_list())
		music = list(map(lambda x:x[:4]+(timezone.localtime(x[4]).strftime("%A, %d. %B %Y %I:%M%p"),)+x[5:],music))
		return HttpResponse(json.dumps(music,cls=DjangoJSONEncoder))
def test(request):
	timezone.activate(pytz.timezone("Asia/Shanghai"))
	music = list(mapmusic.objects.all().values_list())
	print(list(map(lambda x:x[:4]+(timezone.localtime(x[4]),)+x[5:],music)))
	print(timezone.get_current_timezone())
	print(timezone.localtime(timezone.now()))
	return render(request,'base.html')
