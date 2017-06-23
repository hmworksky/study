#coding:UTF-8
import sys
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.views.generic import RedirectView
import json,urllib,urllib2
from _mysql import NULL
from django.http.response import JsonResponse
import multiprocessing,threading,os,requests
import MySQLdb
from books.models import *
from sign.models import User

def dbtest(request):
    if request.method == 'POST' :
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        result = User.objects.filter(username = uname,password = pwd)
        if result :
            return HttpResponse("success")
        else :
            return HttpResponse("false") 
    return render_to_response('login/login.html')
    

def bejson(request):
    if request.method == 'POST' :
        json_before = request.POST.get('json_before','')
        json_finished = json.dumps(json_before)
        response =  HttpResponseRedirect('/results/')
        request.session['json_f'] = json_finished
        #return HttpResponse("111")
        return response 
    else :
        return render_to_response('includes/tools.html')
def results(request):
        #return HttpResponse("222")
        data = request.session.get('json_f')
        return render_to_response('includes/result.html',{'test_result':data})
     
def database(request):
    datas = databaseget()
    test_result = datas
    li = [1,2,3]
    list = {"a":1,"b":2}
    list01 = list.values()
    return render_to_response('includes/data.html',{'test_result':test_result,'data_name':list})
    
def databaseget():
    li = []
    sql = "select  * from sign_user;"
    conn = MySQLdb.connect(host = '106.14.153.153',user = 'root',passwd = 'test1324',port = 33306 ,db = 'test',charset = 'utf8')
    cursor = conn.cursor()
    cursor.execute(sql)
    f = cursor.fetchall()
    for i in f :
        li.append(i[0])
    return li 
    
    
def post_url(request):
    method = request.method
    if method == 'POST' :
        post_u = request.POST.get('post_url','')
        post_d = request.POST.get('post_data','')
        thread_label = request.POST.get('thread_label','')
        thread_num = request.POST.get('post_thread_num','')
        datas = {'post_u':post_u,'post_d':post_d,'thread_num':thread_num,'method':'POST'}
        post_result = http_method(method,post_u,thread_label,thread_num,post_d)
        return HttpResponse(post_result) 
    
def http_post(post_url,post_data):
    req = urllib2.Request(url = post_url,data = post_data)
    res = urllib2.urlopen(req)
    return res
def http_get(url):
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res
    
def http_method(method,url,flag,num,data = None):
    if method == 'POST' :
        if flag == '0' : 
            res = http_post(url,data)
            return res
        elif flag == '1' :
            res = http_thread_post(num, url, data)
            return res
        elif flag == '2' :
            res = http_multi_post(num, url, data)
        else :
            raise_error()
    elif method == 'GET' :
        if flag == '0' :            
            res = http_get(url)
        elif flag == '1' :
            res = http_thread_get(num, url)
            return res
        elif flag == '2' :
            res = http_multi_get(num, url)
            return res
        else :
            raise_error()



def test_req(request):
    if request.method == 'POST' :
        return request.POST
    elif request.method == 'GET' :
        return request.Get()            
        
 
def http_thread_post(num,url,data):
    count = 0
    num = int(num)
    for i in range(num) :
        t = threading.Thread(target = http_post , args = (url,data))
        t.start()
        count += 1
    msg = "%d thread finished" % count
    return msg

def http_thread_get(num,url):
    count = 0
    num = int(num)
    for i in range(num) :
        t = threading.Thread(target = http_get , args = (url,))
        t.start()
        count += 1
    msg = "%d thread finished" % count
    return msg
    
def http_multi_get(num,url):
    num = int(num)
    for i in range(num) :
        process = multiprocessing.Process(target = http_get,args = (url,))
        process.start()
        
def http_multi_post(num,url,data):
    num = int(num)
    for i in range(num) :
        process = multiprocessing.Process(target = http_post,args = (url,data))
        process.start()

        
def raise_error():
      raise TypeError ,'Type error'

def test_model():
    p = Publisher(name = 'haha')
    p.save()
if __name__ == '__main__' :
    databaseget()

    
    
    