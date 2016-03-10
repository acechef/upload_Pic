# coding:utf-8 
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import simplejson,os,time
from django.conf import settings
import yanzhengma
from myform.models import IP,Dream

def index(request):
    code_img = yanzhengma.create_validate_code()
    code_img[0].save("./myform/static/css/validate.png", "PNG")
    return render_to_response('form.html',locals())

def test(request):
    '''
    获得文件上传请求
    '''
    file= request.FILES['file']
    print(file)
    result,new_name=profile_upload(file)
    if result:
        json={'flag':'ok','pic_name':new_name}
    else:
        json={'flag':'no'}
    return HttpResponse(simplejson.dumps(json,ensure_ascii = False))
def profile_upload(file):  
    '''文件上传函数'''  
    if file:  
        path=settings.MEDIA_ROOT 
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
    code_img[0].save("./myform/static/css/validate.png", "PNG")
    image_data = open("./myform/static/css/validate.png","rb").read()
    response = HttpResponse(image_data, content_type="image/png")
    #将验证码存储进session
    request.session['vcode'] = code_img[1].lower()
    return response

# def verificeVCode(request):
#     '''
#     验证码校验BootstrapValidator
#     '''
#     yourVCode=request.POST.get('yourVCode')
#     json_data={'flag':'0'}
#     if(yourVCode.lower()==request.session.get('vcode',default=None)):
#         json_data['flag']='1'
#         print (simplejson.dumps(json_data,ensure_ascii = False))
#     return HttpResponse(simplejson.dumps(json_data,ensure_ascii = False))

def verificeVCode(request):
    '''
    验证码校验 Jquery validate
    '''
    yourVCode=request.POST.get('captcha')
    if(yourVCode.lower()==request.session.get('vcode',default=None)):
        return HttpResponse("true")
    else:
        return HttpResponse("false")

def saveDream(request):
    '''
    保存dream信息
    '''
    username=request.POST.get('username')
    email=request.POST.get('email')
    content=request.POST.get('want')
    pic_name=request.POST.get('pic_name')
    try:
    	ip_address=request.META['HTTP_X_FORWARDED_FOR']
    	ip_address=ip_address.split(",")[0]
    except Exception, e:
    	try:
    		ip_address = request.META['REMOTE_ADDR']
    	except Exception, e:
    		ip_address=""
    ip=IP.objects.create(ip_address=ip_address)
    dream=Dream()
    dream.name=username
    dream.email=emailHttpResponse("false")
    dream.content=content
    dream.pic_name=pic_name
    dream.ip=ip
    dream.save()
    return HttpResponseRedirect('fly_success.html')

def fly_success(request):
    return render_to_response('fly_success.html')

def followdream(request):
    try:
        ip_address=request.META['HTTP_X_FORWARDED_FOR']
        ip_address=ip_address.split(",")[0]
    except Exception, e:
        try:
            ip_address = request.META['REMOTE_ADDR']
        except Exception, e:
            ip_address=""
    ip=ip_address
    dreams=Dream.objects.order_by('-create_time')[:5]
    return render_to_response('followdream.html',locals())

def support_it(request):
    dream_id=request.POST.get('dream_id')
    ip=request.POST.get('ip')
    #在ip表查询是否ip与id对应上的记录，若存在则删除记录;若不存在，则添加记录
    return HttpResponse("false")
