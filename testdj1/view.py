# -*-coding:utf-8 -*-
#coding:UTF-8

'''
Created on 2017��5��22��

@author: huangmin
'''

from django.template.loader import get_template
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import Template
import datetime
from django.template import Context
from multiprocessing.util import get_temp_dir
from django.shortcuts import render_to_response
import json
import Cookie
from django.http.response import JsonResponse
from books import *
from dss.Serializer import serializer
from books.models import Publisher
# import sys
# default_eccoding = 'utf-8'
# if sys.getdefaultencoding() != default_eccoding:
#     reload(sys)
#     sys.setdefaultencoding = default_eccoding

def hello(request):
    ctime = datetime.datetime.now()
    html = "<html><body> It is now %s </body></html>" %ctime
    return HttpResponse(html)
     
def request_post(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        return HttpResponse(uid)
    
def jsontest(request):
    str = {"a":1,"b":2}
    return JsonResponse(str)

def hellodate(request,offset):
    try :
        offset = int(offset)
    except ValueError :
        raise Http404()
    begintime = datetime.datetime.now()
    endtime = datetime.datetime.now()+datetime.timedelta(hours = offset)
    return render_to_response('hours_ahead.html',{'hour_offset':begintime,'next_time':endtime})
def current_html(request):
    times = datetime.datetime.now()
#    t = get_template('index.html')
#    html = t.render(Context({'current':times}))
#    return render_to_response('index.html', {'current':times})
    return render_to_response('index.html', locals())
def current_nav(request):
    times = datetime.datetime.now()
    return render_to_response('includes/nav.html', {'current_date':times})

def return_interface(request):
    a = {"name1":"111","name2":"222"}
    b = json.dumps(a)
    return HttpResponse(b)
def login_action(request):
    try :
        if request.method == 'POST' :
            username = request.POST.get('loginName','')
            response = HttpResponseRedirect('/management/')
            #response.set_cookie('user',username,300)
            request.session['user'] = username
            return response
        else :
            return render_to_response('includes/login.html')
    except Exception ,e :
        return e
    
def management(request):
    session = request.session.get('user')
    return render_to_response('includes/management.html',{'session':session})

def migra():
    ac_list = Publisher.objects.all()
    data = serializer(ac_list)

def login(request):
    return render_to_response('login/signup.html')
             
def readhtml(request):
    html = request.get("http://10test71.stg3.1768.com/branch.txt")
    html.read()
    for i in html :
        print i 
if __name__ == '__main__' :
     readhtml()
        