# -*- coding: utf-8 -*-
import urllib,datetime
from time import sleep
import re,urllib2,urllib
from conn import opendb
from bs4 import BeautifulSoup
#from makepolo.makepolo.spiders.urltest import web_url
db = opendb()
cursor=db.cursor()
from scrapy.selector import Selector
try:  
    from scrapy.spider import Spider  
except:  
    from scrapy.spider import BaseSpider as Spider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from makepolo.items import MakepoloItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class dmozSpider(CrawlSpider):
    name = "hdpe"
    download_delay = 1
    allowed_domains = ["makepolo.com"]
    start_urls=["http://china.makepolo.com/list/spc146099/1/",]
    rules=[
           #Rule(SgmlLinkExtractor(allow=(r'http://www.ccedip.com/product/gongy.asp\?style=0&bigclass=&k=PA66&px=1&province=&city=&days=30&pagenum=20&page=\d+')),follow=True), 
           #Rule(SgmlLinkExtractor(allow=(r'http://www.ccedip.com/product/gypar_\d+.html')),callback="parse_item"), 
           Rule(SgmlLinkExtractor(allow=(r'http://china.makepolo.com/list/spc146099/\d+/')),follow=True), 
           Rule(SgmlLinkExtractor(allow=(r'http://china.makepolo.com/product-detail/\d+.html')),callback="parse_item"),
        ]
    
    def into(self,company_url):
        sleep(1)
        i_headers = {
                         'Connection': 'Keep-Alive',
                         'Accept':'image/webp,*/*;q=0.8',
                         'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                         "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36"
                         }
        request = urllib2.Request(company_url,headers=i_headers)
        response = urllib2.urlopen(request)
        html=response.read().decode('utf-8', 'ignore')
        #公司简介
        company_abstract=''
        pattern_abstract=re.compile(r'<p class="font_14">(.*?)</pre></p>',re.S)
        res_abstract=re.findall(pattern_abstract,html)
        if res_abstract:
            #print res_abstract[0]
            company_abstract = re.sub("<[^>]*?>","",res_abstract[0])
            company_abstract=re.sub(r"\n[\s| ]*\n", '', company_abstract)
            company_abstract=company_abstract.replace(" ","").replace('\n','').replace('\r','').strip()
            company_abstract=str(company_abstract)
            company_abstract=' '.join(company_abstract.split())
            company_abstract=company_abstract.replace(" ","")
            #print company_abstract
        #电话，手机
        
        
        #公司名称，地址，主营产品  
        main_sale1=''  
        #main_sale=''
        pattern_main_sale1=re.compile(r'<div class="base_info">(.*?)<div class="base_info">',re.S)
        res_main_sale1=re.findall(pattern_main_sale1,html)
        if res_main_sale1:
            #print res_main_sale1[0]
            pattern_main_sale=re.compile(r'<ul>(.*?)</ul>',re.S)
            res_main_sale=re.findall(pattern_main_sale,res_main_sale1[0])
            if res_main_sale:
                info=res_main_sale[0]
                #print info
                a=info.split('</li>')
                #for b in a:
                company=a[0]
                Addr=a[2]
                main_sale=a[7]
        company=company.split('：')
        Addr=Addr.split('：')
        main_sale=main_sale.split('：')
        
        return {'company_abstract':company_abstract,'company_name':company[1],'Addr':Addr[1],'main_sale':main_sale[1]}
        
    
    def parse_item(self,response):
        sel = Selector(response)
        web_url=''
        item['web_url']=''
        web_url=str(response)
        if '200' in web_url:
            web_url=re.sub("<200","",web_url)
            web_url=re.sub(">","",web_url)
            web_url=web_url.strip()
        item['web_url']=web_url
        html=response.body.decode('utf-8', 'ignore')
        items=[]
        item=MakepoloItem()
        item['Product_name']=sel.xpath("//*[@class='pd_title']/text()").extract()[0].decode('utf-8', 'ignore')
        item['Location']=sel.xpath("//*[@id='com_city_1']/text()").extract()[0].decode('utf-8', 'ignore')
        item['Linkman']=sel.xpath("//*[@id='div_contact_person_url']/text()").extract()[0].decode('utf-8', 'ignore')
        item['Price']=sel.xpath("//*[@class='pd_info_supplier']/li[4]/span/text()").extract()[0].decode('utf-8', 'ignore')
        try:
            item['Mobile']=sel.xpath("//*[@id='pd_info_contact']/li[1]/span[1]/text()").extract()[0].decode('utf-8', 'ignore')
        except:
            item['Mobile']=''
        try:
            item['Tel']=sel.xpath("//*[@id='pd_info_contact']/li[1]/span[2]/text()").extract()[0].decode('utf-8', 'ignore')
        except:
            item['Tel']=''
        item['company_url']=''
        item['company_url']=sel.xpath("//*[@id='com_name_1']/@href").extract()[0].decode('utf-8', 'ignore') 
        company_url=str(item['company_url'])
        company_url=company_url+'/corp/corp.html'
        messagelist=self.into(company_url)
        item['Company_name']=messagelist['company_name']
        item['Addr']=messagelist['Addr']
        item['company_abstract']=messagelist['company_abstract']
        item['main_sale']=messagelist['main_sale']
        
        Factory=''
        Brand=''
        Lei=''
        Sales_mode=''
        Processing_level=''
        Characteristic_level=''
        Application_level=''
        item['Factory']=''
        item['Brand']=''
        item['Lei']=''
        item['Sales_mode']=''
        item['Processing_level']=''
        item['Characteristic_level']=''
        item['Application_level']=''

        pattern_table_info=re.compile(r'<div class="pd_param clearfix">(.*?)<div class="pd_content">',re.S)
        res_table_info=re.findall(pattern_table_info,html)
        if res_table_info:
            #print res_table_info[0]
            pattern_tablecut=re.compile(r'<ul>(.*?)</ul>',re.S)
            res_tablecut=re.findall(pattern_tablecut,res_table_info[0])
            if res_tablecut:
                info=res_tablecut[0]
                a=info.split('</li>')
                listinfo=[]
                for b in a:
                    #print b
                    if '</span>' in b:
                        listinfo.append(b)
                        #print listinfo
                for c in listinfo:
                    if '产地' in c:
                        Factory=c.split('：')[1]
                    if '品牌/厂家：' in c:
                        Factory=Factory+c.split('：')[1]
                    if '牌号：' in c:
                        Brand=c.split('：')[1]
                    if '类型：' in c:
                        Lei=c.split('：')[1]
                    if '销售方式：' in c:
                        Sales_mode=c.split('：')[1]
                    if '加工级别：' in c:
                        Processing_level=c.split("：")[1]
                    if '特性级别：' in c:     
                        Characteristic_level=c.split("：")[1]
                    if '用途级别：' in c:     
                        Application_level=c.split("：")[1]
        item['Factory']=Factory
        item['Brand']=Brand
        item['Lei']=Lei
        item['Sales_mode']=Sales_mode
        item['Processing_level']=Processing_level
        item['Characteristic_level']=Characteristic_level
        item['Application_level']=Application_level
        #详细信息
        Details=''
        item['Details']=''
        pattern_detailbig=re.compile(r'<div class="pd_content">(.*?)<div class="pd_prompt">',re.S)
        res_detailbig=re.findall(pattern_detailbig,html)
        if res_detailbig:
            #print res_detailbig[0]
            pattern_detail=re.compile(r'<div id="detail_dfp_d_5">(.*?)-->',re.S)
            res_detail=re.findall(pattern_detail,res_detailbig[0])
            if res_detail:
                #print res_detail[0]
                Details=re.sub("<[^>]*?>","",res_detail[0])
                Details = re.sub("&nbsp;","",Details)
                Details=re.sub(r"\n[\s| ]*\n", '', Details)
                Details=Details.replace(" ","").replace('\n','').replace('\r','').strip()
                #print Details
        item['Details']=Details
        """
        #匹配出图片html
        item['picnamestring']=''
        picnamestring=''
        pattern_picall=re.compile(r'<ul class="pd_slide_tab_pic">(.*?)<s class="pd_slide_arr_r">',re.S)
        res_picall=re.findall(pattern_picall,html)
        if res_picall:
            pichtml=res_picall[0]
            #print pichtml
            #匹配出图片地址
            pattern_picurl=re.compile(r'<img src="(.*?)" onload=',re.S)
            res_picurl=re.findall(pattern_picurl,pichtml)
            if res_picurl:
                #print res_picurl
                for list in res_picurl:
                    #picname=list[26:]
                    picname=list.split('/')
                    picname1=picname[9]
                    picname2=picname[9]
                    picname2=picname2+'|'
                    picnamestring=picnamestring+picname2
                    url=list
                    local = '/home/xbin/图片/MakePolo/ABS_PC/'+picname1
                    urllib.urlretrieve(url,local)
        item['picnamestring']=picnamestring
        """
        #匹配出图片html
        item['picnamestring']=''
        picnamestring=''
        pattern_picall=re.compile(r'<ul class="pd_slide_tab_pic">(.*?)<s class="pd_slide_arr_r">',re.S)
        res_picall=re.findall(pattern_picall,html)
        if res_picall:
            pichtml=res_picall[0]
            #print pichtml
            soup=BeautifulSoup(pichtml)
            li_list=soup.findAll('li')
            #print li_list
            l=len(li_list)
            pic_url_list=[]
            #web_url='http://china.makepolo.com/product-detail/100465009180'
            web_url2=re.sub('.html','',web_url)
            for n in range(0,l):
                pic_url=web_url2+'_'+str(n)
                pic_url=re.sub('detail','picture',pic_url)
                #pic_url2=pic_url.replace('detail','picture')
                pic_url=pic_url+'.html'
                #print pic_url
                pic_url_list.append(pic_url)
            for pic_big_url in pic_url_list:
                print pic_big_url   
                pic_name=pic_big_url[42:-5]
                pic_name=pic_name+'.jpg'
                print pic_name
                
                i_headers2= {
                     'Connection': 'Keep-Alive',
                     'Accept':'image/webp,*/*;q=0.8',
                     'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                     "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36"
                     }
                
                request2=urllib2.Request(pic_big_url,headers=i_headers2)
                response2=urllib2.urlopen(request2)
                html2=response2.read().decode('utf-8', 'ignore')
                
                pattern_picurl1=re.compile(r'<div class="rp_slide_pic_con">(.*?)<div class="rp_slide_pic_r">',re.S)
                res_picurl1=re.findall(pattern_picurl1,html2)
                if res_picurl1:
                    print res_picurl1[0]
                    pattern_picurl=re.compile(r'<img src="(.*?)" onload',re.S)
                    res_picurl=re.findall(pattern_picurl,res_picurl1[0])
                    if res_picurl:
                        print res_picurl[0]
                        pic_name2=pic_name+'|'
                        picnamestring=picnamestring+pic_name2
                        url=res_picurl[0]
                        local = '/home/xbin/图片/MakePolo_new/HDPE/'+pic_name
                        urllib.urlretrieve(url,local)
        item['picnamestring']=picnamestring
        
        
        
        #创建时间
        gmt_created=datetime.datetime.now()
        item['gmt_created']=gmt_created
        
        
        sql="insert into HDPE (web_url,Product_name,gmt_created,Location,Price,Factory,Brand,Lei,Sales_mode,Processing_level,Characteristic_level,Application_level,Details,Linkman,Company_name,Mobile,Tel,Addr,picnamestring,main_sale,company_abstract)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,[item['web_url'],item['Product_name'],item['gmt_created'],item['Location'],item['Price'],item['Factory'],item['Brand'],item['Lei'],item['Sales_mode'],item['Processing_level'],item['Characteristic_level'],item['Application_level'],item['Details'],item['Linkman'],item['Company_name'],item['Mobile'],item['Tel'],item['Addr'],item['picnamestring'],item['main_sale'],item['company_abstract']])
        db.commit()
        
        print item['web_url']
        print item['Product_name']
        print item['Location']
        print item['Price']
        print item['Factory']
        print item['Brand']
        print item['Lei']
        print item['Sales_mode']
        print item['Processing_level']
        print item['Characteristic_level']
        print item['Application_level']
        print item['Details']
        print item['Linkman']
        print item['Company_name']
        print item['Mobile']
        print item['Tel']
        print item['Addr']
        print item['company_abstract']
        print item['main_sale']

        return items
        
        
        
        
        
        