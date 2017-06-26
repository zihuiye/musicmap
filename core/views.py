from django.shortcuts import render
from django.http import  HttpResponseRedirect,HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.conf.urls import url
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
import pytz


import json
# from django.core.serializers import serialize

from .models import mapmusic
# Create your views here.

def index(request):
	return render(request,'index.html')
def music(request):
	if request.method == 'POST':
		musicFile =request.FILES.get("musicFile", None)
		print(musicFile)
		try:
			music = mapmusic.objects.create(
			musicname=request.POST["musicname"],
			lat=request.POST["lat"],lng=request.POST["lng"],
			uploaderemail=request.POST["uploaderemail"],text=request.POST["descript"],
			musicfile=musicFile)
			music.save()
		except Exception as e:
			print(e)
		print(request.POST)
		return HttpResponseRedirect(reverse('index'))
	elif request.method == 'GET':
		timezone.activate(pytz.timezone("Asia/Shanghai"))
		music = list(mapmusic.objects.filter(display=True).values_list())
		music = list(map(lambda x:x[:5]+(timezone.localtime(x[5]).strftime("%A, %d. %B %Y %I:%M%p"),)+x[6:],music))
		return HttpResponse(json.dumps(music,cls=DjangoJSONEncoder))
def test(request):
	timezone.activate(pytz.timezone("Asia/Shanghai"))
	music = list(mapmusic.objects.all().values_list())
	print(list(map(lambda x:x[:4]+(timezone.localtime(x[4]),)+x[5:],music)))
	print(timezone.get_current_timezone())
	print(timezone.localtime(timezone.now()))
	return render(request,'base.html')

def email(request):
	if request.method =="POST":
		subject="来自《音乐地图》管理员的消息"
		message="您好！这是来自《音乐地图》(musicmap.zihuiye.com)管理员的消息。您在本网站在"+ \
		request.POST['uploadtime']+"上传的"+request.POST['musicname']+"有如下的问题：" \
		+request.POST['reviewtext']+" 请回复邮件联系管理员来帮你修改。谢谢！"
		email=request.POST['email']
		try:
			send_mail(subject, message, 'ye.zihui@mail.scut.edu.cn', [email])
		except BadHeaderError:
			return HttpResponse('发现无效的header！')
		except Exception:
			return HttpResponse('发送失败！')
		return HttpResponse('发送成功！')

	return HttpResponse('get mail')
	# subject = request.POST.get('subject', '')
    # message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['admin@example.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('/contact/thanks/')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')
