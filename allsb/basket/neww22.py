from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
#from jinja2 import  Template
from .models import *

# Create your views here.
menu = ['OSaite','Dobavit statio', 'Obratnaya svyaz', 'voite']

def index(request):
    #playertt =  Indextable.objects.only('player','pts','data')
    playertt = Indextable.objects.values('player', 'pts', 'data')
    playertq = Indextable.objects.values('player', 'pts', 'data').filter(player='Kevon Looney')
    playert = list()# список игроков Indextable.objects.values
    rez= dict()
    rt =  list()
    for l in playertt:
        if l['player'] not in playert:
            playert.append(l['player'])
    my_list = ['Kevon Looney', 'Jayson Tatum']
    for lp in playert:
        rt = list()
        #rt.pop()
        playert4 = Indextable.objects.values('pts').filter(player=lp)#[14:]
        for s in playert4:
            rt.append(s['pts'])
            #rt.reverse()
            rez[lp] = rt[::-1]

    '''
    playert = dict() #убираем цыклом повторяющиеся имена, дистинкт не работает
    for ite in playertt:
        if ite.player  not in playert:
            playert[ite] = ite
            #playert[item.pts] = item
            #playert[item.data] = item
            i = i+1'''
    #if item.player  not in playert:
    # playert[item.player] = item
    #plist = dict.items(playert)
    my_list = ['Kevon Looney','Jayson Tatum']
    for ite in my_list:
        playert3= Indextable.objects.filter(player=ite)[5:]
        posts = Indextable.objects.filter(player='Kevon Looney')[10:]
        men = Indextable.objects.filter(player='Jayson Tatum')[10:]#'Jayson Tatum'
        slovar = {'playertt' :playertt,
                  'playert' :playert,
                  'playert3': playert3,
                  'playert4': playert4,
                  'playertq': playertq,
                  'rez': rez,
                  'rt': rt,
                  'posts' : posts,
                  'men': men,
                  'menu' : menu,
                  'title': 'O Saite',
                  'title': 'Glavna stranica'
        }
        return render(request,'basket/index.html',context=slovar)

def about(request):
    trotow = T4.objects.values('p3listvizit')
    #indpl = []
    i5l=[]
    rez2 = dict()
    sppl = []
    spplk =[]
    sp2=[]
    for i in trotow:
        if i['p3listvizit'] not in sppl:
            i['p3listvizit']=i['p3listvizit'].replace(',','\n')
            i['p3listvizit'] = i['p3listvizit'].rstrip()
            i['p3listvizit'] = i['p3listvizit'].lstrip()
            i['p3listvizit']=i['p3listvizit'].splitlines()
            sppl.append(i['p3listvizit'])


    for i in sppl:
        for i2 in i:
           rt2 = list()
           i2.rstrip()
           sppl2=i2.lstrip()
           indpl=Indextable.objects.values('pts').filter(player=sppl2)
           for i5 in indpl:
               i5l.append(i5['pts'])
           f=i2 +str(i5l)#.replace('<QuerySet',' ').replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ')

           spplk.append(f)
           i5l = []
        sp2.append(spplk)
        spplk = []
           # for i3 in indpl:
           #     rt2.append(i3['pts'])
           #     rez2[i2] = rt2[::-1]

    slovar = {'trotow': trotow,
              'sppl': sppl,
              'indpl': indpl,
              'sppl2': sppl2,
              'rez2': rez2,
              'sp2': sp2,
              'menu': menu,
              'title': 'O Saite',
              'title': 'Glavna stranica'
              }
    return render(request,'basket/about.html',context=slovar)

def base(request):
    return render(request,'basket/base.html',{ })

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Страница прилож  баскет</h1>{catid}')

def pageNotFound(request, exception):
    print(request.GET)
    return HttpResponseNotFound('<h1>404 errorrr</h1>')