#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import simplejson,os,time
from django.conf import settings

def index(request):
	# return HttpResponse(u"hsayudh!")
	return render_to_response('form.html',locals())


def a(request):
	return render_to_response('a.html',locals())

# def test(request):
#     file= request.FILES['file']
#     if file:  
#     	result,new_name=profile_upload(file)  
#     	if result:  
#     		ret="1"  
#     	else:  
#     		ret="2" 
#     json={'ret':ret,'save_name':new_name}  
#     return HttpResponse(simplejson.dumps(json,ensure_ascii = False))

def test(request):
    file= request.FILES['file']
    result,new_name=profile_upload(file)
    if result:
        json={'flag':'ok','pic_name':new_name}
    else:
        json={'flag':'no'}
    return HttpResponse(simplejson.dumps(json,ensure_ascii = False))
def profile_upload(file):  
    '''''文件上传函数'''  
    if file:  
        path='/home/zjq/'+'upload' 
        # path=os.path.join(settings.MEDIA_ROOT,'')
        # file_name=file.name
        suffix=(file.name).split()[-1]
        file_name=str(int(time.time()))+suffix
        path_file=os.path.join(path,file_name)
        print(path_file)
        fp = open(path_file, 'wb')  
        for content in file.chunks():   
            fp.write(content)  
        fp.close()  
        return (True,file_name) #change  
    return (False,file_name)   #change

def jQueryFileUpload(request):
    return render_to_response('jQueryFileUpload.html',locals())

def baidu(request):
    return render_to_response('baidu.html',locals())

def picture(request):
    return render_to_response('picture.html',locals())