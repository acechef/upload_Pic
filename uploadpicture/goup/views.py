#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import simplejson,os
from django.conf import settings

def index(request):
	# return HttpResponse(u"hsayudh!")
	return render_to_response('form.html',locals())
