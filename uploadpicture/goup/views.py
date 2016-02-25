#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import simplejson,os,time
from django.conf import settings
import yanzhengma

def index(request):
    code_img = yanzhengma.create_validate_code()
    code_img[0].save("./goup/static/css/validate.gif", "GIF")
    return render_to_response('form.html',locals())

def test(request):
    '''
    获得文件上传请求
    '''
    file= request.FILES['file']
    result,new_name=profile_upload(file)
    if result:
        json={'flag':'ok','pic_name':new_name}
    else:
        json={'flag':'no'}
    return HttpResponse(simplejson.dumps(json,ensure_ascii = False))
def profile_upload(file):  
    '''文件上传函数'''  
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

def getVCode(request):
    '''
    点击换一张时生成新的验证码
    '''
    code_img = yanzhengma.create_validate_code()
    code_img[0].save("./goup/static/css/validate.gif", "GIF")
    return HttpResponse('ok')

def jQueryFileUpload(request):
    return render_to_response('jQueryFileUpload.html',locals())

def baidu(request):
    return render_to_response('baidu.html',locals())

def picture(request):
    return render_to_response('picture.html',locals())