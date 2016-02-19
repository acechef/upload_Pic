#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import simplejson,os
from django.conf import settings

def index(request):
	# return HttpResponse(u"hsayudh!")
	return render_to_response('form.html',locals())

def UploadHandler(request):
	file = request.FILES.get("Filedata",None)
	if file:  
		result,new_name=profile_upload(file)  
		if result:  
			ret="1"  
		else:  
			ret="2" 
	json={'ret':ret,'save_name':new_name}  
	return HttpResponse(simplejson.dumps(json,ensure_ascii = False))



def a(request):
	return render_to_response('a.html',locals())

def test(request):
	file = request.FILES.get("Filedata",None)
	if file:  
		result,new_name=profile_upload(file)  
		if result:  
			ret="1"  
		else:  
			ret="2" 
	json={'ret':ret,'save_name':new_name}  
	return HttpResponse(simplejson.dumps(json,ensure_ascii = False))

def profile_upload(file):  
    '''''文件上传函数'''  
    if file:  
        # path='/home/zjq/'+'upload' 
        path=os.path.join(settings.MEDIA_ROOT,'upload')
        #file_name=str(uuid.uuid1())+".jpg"  
        file_name=file.name  
        #fname = os.path.join(settings.MEDIA_ROOT,filename)  
        path_file=os.path.join(path,file_name)  
        fp = open(path_file, 'wb')  
        for content in file.chunks():   
            fp.write(content)  
        fp.close()  
        return (True,file_name) #change  
    return (False,file_name)   #change