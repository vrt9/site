from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime
#from jinja2 import  Template
from .models import *

# Create your views here.
menu = ['OSaite','Dobavit statio', 'Obratnaya svyaz', 'voite']

# def index(request):
#     #playertt =  Indextable.objects.only('player','pts','data')
#     playertt = Indextable.objects.values('player', 'pts', 'data')
#     playertq = Indextable.objects.values('player', 'pts', 'data').filter(player='Kevon Looney')
#     playert = list()# список игроков Indextable.objects.values
#     rez= dict()
#     rt =  list()
#     for l in playertt:
#         if l['player'] not in playert:
#             playert.append(l['player'])
#     my_list = ['Kevon Looney', 'Jayson Tatum']
#     for lp in playert:
#         rt = list()
#         #rt.pop()
#         playert4 = Indextable.objects.values('pts').filter(player=lp)#[14:]
#         for s in playert4:
#             rt.append(s['pts'])
#             #rt.reverse()
#             rez[lp] = rt[::-1]
#
#     '''
#     playert = dict() #убираем цыклом повторяющиеся имена, дистинкт не работает
#     for ite in playertt:
#         if ite.player  not in playert:
#             playert[ite] = ite
#             #playert[item.pts] = item
#             #playert[item.data] = item
#             i = i+1'''
#     #if item.player  not in playert:
#     # playert[item.player] = item
#     #plist = dict.items(playert)
#     my_list = ['Kevon Looney','Jayson Tatum']
#     for ite in my_list:
#         playert3= Indextable.objects.filter(player=ite)[5:]
#         posts = Indextable.objects.filter(player='Kevon Looney')[10:]
#         men = Indextable.objects.filter(player='Jayson Tatum')[10:]#'Jayson Tatum'
#         slovar = {'playertt' :playertt,
#                   'playert' :playert,
#                   'playert3': playert3,
#                   'playert4': playert4,
#                   'playertq': playertq,
#                   'rez': rez,
#                   'rt': rt,
#                   'posts' : posts,
#                   'men': men,
#                   'menu' : menu,
#                   'title': 'O Saite',
#                   'title': 'Glavna stranica'
#         }
#         return render(request,'basket/index.html',context=slovar)

def index(request):

    def kalendar(dt, p3_t, p_el5):
        t = datetime.datetime.today() - datetime.timedelta(dt)
        p3datkal = t.date()
        p3datkal = p3datkal.strftime("%d.%m.%Y")
        # p3datkal = datetime.datetime.now()
        # p3datkal = p3datkal.date().strftime("%d.%m.%Y")
        kalendarbd = Bdgameday.objects.values_list('p3teamviz','p3teamhome','p3date').filter(p3date=p3datkal)
        #comTgdh = Tablegameday.objects.values_list('p3teamhome', flat=True).filter(p3date=p3dat)
        listKbd = [i for j in kalendarbd for i in j]# делаем список вчерашних игр из queryset
        tvizlist = []
        for i in el2:
            if p3_t in i: # ищем в словаре ключ 'p3teamviz'
                if i[p3_t] in listKbd: #если значение ключа (название команды) есть в списке комманд
                    print(i[p3_t])
                    for k in kalendarbd:
                        if i[p3_t] in k:
                            print(k)  # получаем с кем играла комманда
                            tvizlist.append(k)
        print('qqqqqqq',tvizlist)
        for i in p_el5:
            print(i[p3_t])
            print(i)
            print(type(i))
            #if i['p3teamviz'] in tvizlist:
            for t in tvizlist:
                    if i[p3_t] in t:
                        tt = list(t)  # преобразовываем кортеж в список
                        tt[0], tt[2] = tt[2], tt[0]  # ставим дату вперед
                        tt[1] = tt[1] + ' - ' + tt[2]  # добавляем пробел и соединяем две команды
                        tt.pop(-1)  # удаляем лишний элемент, остался после соединения
                        tt =  ' \xa0 \xa0  '.join(tt)
                        i[dt] = tt
                        # i['klnd'] = ' \xa0 \xa0  '.join(i['klnd'])  # добавляем пробелов и переводим в строку
                        print(i)

                        # tt = '  '.join(tt)  # добавляем пробелов и переводим в строку
                        # sptt.append(tt)
                        # i['klnd'] = sptt
                        # # i['klnd'] = ' \xa0 \xa0  '.join(i['klnd'])  # добавляем пробелов и переводим в строку
                        # print(i)

        # for i in el2:
        #     if 'p3teamhome' in i:
        #         if i['p3teamhome'] in listKbd:
        #             print(i['p3teamhome'])
        #             for k in kalendarbd:
        #                 if i['p3teamhome'] in k:
        #                     print(k, 'home')

    p3dat = datetime.datetime.now()
    p3dat = p3dat.date().strftime("%d.%m.%Y")
    trotow = Tablegameday.objects.values('p3listvizit').filter(p3date=p3dat)
    indpl = []
    i5l=[]
    rez2 = dict()
    sppl = []
    sppl3 = []
    spplk = {}
    spplk2 = {}
    sp2=[]
    sp3 = []
    sptt =[]
    # home0 = []
    # home0list2 = []
    # home100list2 = []
    # home75list2 = []
    # home50list2 = []
    # home25list2 = []
    l=0
    l=l+1
    for i in trotow:
        if i['p3listvizit'] not in sppl:
            i['p3listvizit']=i['p3listvizit'].replace(',','\n')
            i['p3listvizit'] = i['p3listvizit'].rstrip()
            i['p3listvizit'] = i['p3listvizit'].lstrip()
            i['p3listvizit']=i['p3listvizit'].splitlines()
            sppl.append(i['p3listvizit'])

    trotow2=Tablegameday.objects.values('p3listhome').filter(p3date=p3dat)
    for i in trotow2:
        if i['p3listhome'] not in sppl3:
            i['p3listhome']=i['p3listhome'].replace(',','\n')
            i['p3listhome'] = i['p3listhome'].rstrip()
            i['p3listhome'] = i['p3listhome'].lstrip()
            i['p3listhome']=i['p3listhome'].splitlines()
            sppl3.append(i['p3listhome'])

    for i in sppl3:
        for i2 in i:
           rt3 = list()
           i2.rstrip()
           i2.lstrip()
           sppl4=i2.lstrip()
           indpl2=Indextable5.objects.values('pts').filter(player=sppl4)

           for i5 in indpl2:
               i5l.append(i5['pts'])
               # f=i2 +str(i5l).replace('<QuerySet',' ').replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ')
               # iz=f

           spplk2[sppl4] = i5l

           i5l = []
        sp3.append(spplk2)
        spplk2 = {}

    for i in sppl:
        for i2 in i:
           rt2 = list()
           i2.rstrip()
           i2.lstrip()
           sppl2=i2.lstrip()
           indpl=Indextable5.objects.values('pts').filter(player=sppl2)

           for i5 in indpl:
               i5l.append(i5['pts'])
               # f=i2 +str(i5l).replace('<QuerySet',' ').replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ')
               # iz=f

           spplk[sppl2] = i5l

           i5l = []
        sp2.append(spplk)
        spplk = {}
           # for i3 in indpl:
           #     rt2.append(i3['pts'])
           #     rez2[i2] = rt2[::-1]
    trotowtime = Tablegameday.objects.values('p3time','p3status','p3teamviz', 'p3teamhome', 'tvizwl', 'thomwl').filter(p3date=p3dat)
    el=[]
    dd=''
    strm=' kkkjllf'
    #str={}
    strr=[]
    qq=[]
    vr=0
    for x in trotowtime:
        qq= str(sp2[vr]).replace('],', '<br>').replace('{', '').replace(']','').replace('[','').replace('}', '')  #+ sp2[x].values())
        strr.append(qq)
        el.append(x)
        el.append(strr)
        vr+= 1
        strr=[]
    # print(x)
    # print(strr)

    ds=len(sp2)
    lll=[]
    for i in  range(ds):
        lll.append(i)

    # for irez in sp2:
    #     for irezzr2 in irez:

    rl=[]
    #iz=[]
    irez2=1
    # for x in lll:
    #     for e, k in sp2[x].items():
    #         print(e,k)
    #         el.append(e)
    #         irez2+=1
    #
    #     print('-------------------')
    #     iz.append(irez2)
    #     print(irez2)
    #     irez2 = 0
    trotowrez=Tablegameday.objects.values('p3time','p3status').filter(p3date=p3dat)
    itog=[]
    spx=0
    itog= Tablegameday.objects.values('p3time','p3listvizit').filter(p3date=p3dat)


    sttr3=[{'p3time': '3:30 PM ET', 'p3status': 'Confirmed Lineup'},
           {'tvizwl': '(7-18)', 'thomwl': '(6-16)'},
           ['\'Mike Conley\': 10, 17, 15, 6, 20, 30, 13, 18, 12, 6, 6, 13, 5, 17 '
            '\'Donovan Mitchell\': 16, 27, 22, 15, 30, 28, 36, 37, 21, 27, 26, 22, 13, 20, 26<br> '
            '\'Bojan Bogdanovic\': 22, 13, 15, 19, 14, 14, 20, 23, 16, 13, 18, 8, 26, 27, 7, 10<br> ']]


    zaprosbdfull=[]
    ptszitog=[]
    com= Tablegameday.objects.values_list('p3teamviz', flat=True).filter(p3date=p3dat)
    for i in com:
        comand = {'CHA':'Charlotte',
                  'NOP':'New Orleans',
                  'UTA':'Utah',
                  'WAS':'Washington',
                  'NYK':'New York',
                  'DET':'Detroit',
                  'CLE':'Cleveland',
                  'ATL':'Atlanta',
                  'TOR':'Toronto',
                  'IND':'Indiana',
                  'LAC':'L.A. Clippers',
                  'BOS':'Boston',
                  'CHI':'Chicago',
                  'LAL':'L.A. Lakers',
                  'MEM':'Memphis',
                  'OKC':'Oklahoma City',
                  'PHX':'Phoenix',
                  'POR':'Portland',
                  'DAL':'Dallas',
                  'SAC':'Sacramento',
                  'BKN':'Brooklyn',
                  'DEN':'Denver',
                  'GSW':'Golden State',
                  'MIA':'Miami',
                  'MIL':'Milwaukee',
                  'MIN':'Minnesota',
                  'ORL':'Orlando',
                  'PHI':'Philadelphia',
                  'SAS':'San Antonio',
                  'HOU':'Houston'}

        zaprosbdfull.append( list(Indextable5.objects.values_list('player', flat=True).filter(status=comand[i]))) # создаем список игроков гостей
    for zaprosbd in zaprosbdfull:
        zaprosbdnew=[]
        pts= {}
        ptsz = {}
        for i in zaprosbd:
            if i not in zaprosbdnew:
                # zaprosbdnew.append(i)
                ptsl = list(Indextable5.objects.values_list('pts', flat=True).filter(player=i))
                ptsl.reverse()
                i = i.replace(', Jr.', '')
                i = i.replace(' Jr.', '')
                i = i.replace(' II', '')
                i = i.replace(' III', '')
                i = i.replace("Jae'sean", "Jae'Sean")
                i = i.replace("B.J. Boston", "Brandon Boston")
                i = i.replace('Herb Jones', 'Herbert Jones')
                i = i.replace('Raulzinho Neto', 'Raul Neto')
                i = i.replace('Jayden Scrubb', 'Jay Scrubb')
                zaprosbdnew.append(i)
                pts[i]=ptsl
                ptsz[i]=round(sum(ptsl) / len(ptsl),1)
                #ptsz[i] =list(ptsz[i])
        # ptsz = sorted(ptsz.items(), key=lambda x: x[1])
        ptsz = dict(sorted(ptsz.items(), key=lambda item: item[1], reverse=True))

        home0 = Tablegameday.objects.values('p3listhome0').filter(p3date=p3dat)
        home0list = []
        for i in home0:
            if i['p3listhome0'] not in home0list:
                i['p3listhome0'] = i['p3listhome0'].replace(',', '\n')
                i['p3listhome0'] = i['p3listhome0'].rstrip()
                i['p3listhome0'] = i['p3listhome0'].lstrip()
                i['p3listhome0'] = i['p3listhome0'].splitlines()
                home0list.append(i['p3listhome0'])
        home0list2 = []
        for i in home0list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                home0list2.append(i3)

        home100 = Tablegameday.objects.values('p3listhome100').filter(p3date=p3dat)
        home100list = []
        for i in home100:
            if i['p3listhome100'] not in home100list:
                i['p3listhome100'] = i['p3listhome100'].replace(',', '\n')
                i['p3listhome100'] = i['p3listhome100'].rstrip()
                i['p3listhome100'] = i['p3listhome100'].lstrip()
                i['p3listhome100'] = i['p3listhome100'].splitlines()
                home100list.append(i['p3listhome100'])
        home100list2 = []
        for i in home100list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                home100list2.append(i3)

        home75 = Tablegameday.objects.values('p3listhome75').filter(p3date=p3dat)
        home75list = []
        for i in home75:
            if i['p3listhome75'] not in home75list:
                i['p3listhome75'] = i['p3listhome75'].replace(',', '\n')
                i['p3listhome75'] = i['p3listhome75'].rstrip()
                i['p3listhome75'] = i['p3listhome75'].lstrip()
                i['p3listhome75'] = i['p3listhome75'].splitlines()
                home75list.append(i['p3listhome75'])
        home75list2 = []
        for i in home75list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                home75list2.append(i3)

        home50 = Tablegameday.objects.values('p3listhome50').filter(p3date=p3dat)
        home50list = []
        for i in home50:
            if i['p3listhome50'] not in home50list:
                i['p3listhome50'] = i['p3listhome50'].replace(',', '\n')
                i['p3listhome50'] = i['p3listhome50'].rstrip()
                i['p3listhome50'] = i['p3listhome50'].lstrip()
                i['p3listhome50'] = i['p3listhome50'].splitlines()
                home50list.append(i['p3listhome50'])
        home50list2 = []
        for i in home50list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                home50list2.append(i3)

        home25 = Tablegameday.objects.values('p3listhome25').filter(p3date=p3dat)
        home25list = []
        for i in home25:
            if i['p3listhome25'] not in home25list:
                i['p3listhome25'] = i['p3listhome25'].replace(',', '\n')
                i['p3listhome25'] = i['p3listhome25'].rstrip()
                i['p3listhome25'] = i['p3listhome25'].lstrip()
                i['p3listhome25'] = i['p3listhome25'].splitlines()
                home25list.append(i['p3listhome25'])
        home25list2 = []
        for i in home25list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                home25list2.append(i3)



        #vizit100list2 = vizit100list2.remove(" ''")
        # vizit100list = []
        # for i in vizit100:

        # home100list2 = []
        # for i in home100list:
        #     for i2 in i:
        #         i3 = i2.rstrip().lstrip()
        #         i3 = i3.replace(',', '')
        #         home100list2.append(i3)
        #

        # home0 = Tablegameday.objects.values('p3listhome0')
        # home0list = []
        # for i in home0:
        #     if i['p3listhome0'] not in home0list:
        #         i['p3listhome0'] = i['p3listhome0'].replace(',', '\n')
        #         i['p3listhome0'] = i['p3listhome0'].rstrip()
        #         i['p3listhome0'] = i['p3listhome0'].lstrip()
        #         i['p3listhome0'] = i['p3listhome0'].splitlines()
        #         home0list.append(i['p3listhome0'])



        # home0 = Tablegameday.objects.values('p3listhome0')

        v=''
        iv='Jalen Green, John Wall, '
        # for i in home0:
        #     if i['p3listhome0'] not in home0list:
        #         i['p3listhome0'] = i['p3listhome0'].replace(',', '\n')
        #         i['p3listhome0'] = i['p3listhome0'].rstrip()
        #         i['p3listhome0'] = i['p3listhome0'].lstrip()
        #         i['p3listhome0'] = i['p3listhome0'].splitlines()
        #         home0list.append(i['p3listhome0'])
        for i in list(ptsz):
            for ii in pts:
                if i == ii:
                    # pts[ii].append(ptsz[i])
                    # ptsz[i] = pts[ii]
                    ptsz[i]= str(ptsz[i]) + '............' + str(pts[ii])
        ptszitog.append(ptsz)

    trotowtime2 = Tablegameday.objects.values('p3time', 'p3status', 'p3teamviz', 'p3teamhome', 'tvizwl', 'thomwl', 'p3status2').filter(p3date=p3dat)
    el2 = []
    el5 = []
    el22v = {}
    el3 = []
    strr2 = []
    qq2 = []
    vr2 = 0
    for x in trotowtime2:
            #qq2 = str(ptszitog[vr])#.replace('],', '<br>').replace('{', '').replace(']', '').replace('[', '').replace('}',
                                                                                                                    # '')  # + sp2[x].values())
            el2.append(x)
            el2.append(ptszitog[vr2])
            el22v.update(x)
            el22v.update(ptszitog[vr2])
            el5.append(el22v)
            el22v = {}
            vr2 += 1
            strr2 = []
            # if i in home0list2:
            #      ptsz['<span style="background:#FFFFCC">' + i + '</span>'] = ptsz.pop(i)  #'<span style="background:#FFFFCC">' + ptsz[i] + '</span>'


            #     for i5 in indpl2:
            #         i5l.append(i5['pts'])
            #         # f=i2 +str(i5l).replace('<QuerySet',' ').replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ')
            #         # iz=f
            #
            #     spplk2[sppl4] = i5l
            #
            #     i5l = []
            # sp3.append(spplk2)
            # spplk2 = {}

            # if i['player'] not in zaprosbdnew:
            #     zaprosbdnew.append(i['player'])
        # for i in zaprosbdnew:
        #     pts=Indextable5.objects.values('pts').filter(player=i)
        #     ptslist=

        #zaprosbd = list(Indextable5.objects.values_list('player', flat=True).filter(status='Toronto'))

    zaprosbdfull = []
    ptszitog = []
    com = Tablegameday.objects.values_list('p3teamhome', flat=True).filter(p3date=p3dat) #берем из тэйблгеймдей домашние команды
    for i in com:
        comand = {'CHA':'Charlotte',
                  'NOP':'New Orleans',
                  'UTA':'Utah',
                  'WAS':'Washington',
                  'NYK':'New York',
                  'DET':'Detroit',
                  'CLE':'Cleveland',
                  'ATL':'Atlanta',
                  'TOR':'Toronto',
                  'IND':'Indiana',
                  'LAC':'L.A. Clippers',
                  'BOS':'Boston',
                  'CHI':'Chicago',
                  'LAL':'L.A. Lakers',
                  'MEM':'Memphis',
                  'OKC':'Oklahoma City',
                  'PHX':'Phoenix',
                  'POR':'Portland',
                  'DAL':'Dallas',
                  'SAC':'Sacramento',
                  'BKN':'Brooklyn',
                  'DEN':'Denver',
                  'GSW':'Golden State',
                  'MIA':'Miami',
                  'MIL':'Milwaukee',
                  'MIN':'Minnesota',
                  'ORL':'Orlando',
                  'PHI':'Philadelphia',
                  'SAS':'San Antonio',
                  'HOU':'Houston'}

        zaprosbdfull.append(list(Indextable5.objects.values_list('player', flat=True).filter(status=comand[i])))
    for zaprosbd in zaprosbdfull:
        zaprosbdnew = []
        pts = {}
        ptsz = {}
        for i in zaprosbd:
            if i not in zaprosbdnew:
                # zaprosbdnew.append(i)
                ptsl = list(Indextable5.objects.values_list('pts', flat=True).filter(player=i))
                ptsl.reverse()
                i = i.replace(', Jr.', '')
                i = i.replace(' Jr.', '')
                i = i.replace(' II', '')
                i = i.replace(' III', '')
                i = i.replace("Jae'sean", "Jae'Sean")
                i = i.replace("B.J. Boston", "Brandon Boston")
                i = i.replace('Herb Jones', 'Herbert Jones')
                i = i.replace('Raulzinho Neto', 'Raul Neto')
                i = i.replace('Jayden Scrubb', 'Jay Scrubb')
                zaprosbdnew.append(i)
                pts[i] = ptsl
                ptsz[i] = round(sum(ptsl) / len(ptsl), 1)
                # ptsz[i] =list(ptsz[i])
        # ptsz = sorted(ptsz.items(), key=lambda x: x[1])
        ptsz = dict(sorted(ptsz.items(), key=lambda item: item[1], reverse=True))

        vizit0 = Tablegameday.objects.values('p3listvizit0').filter(p3date=p3dat)
        vizit0list = []
        for i in vizit0:
            if i['p3listvizit0'] not in vizit0list:
                i['p3listvizit0'] = i['p3listvizit0'].replace(',', '\n')
                i['p3listvizit0'] = i['p3listvizit0'].rstrip()
                i['p3listvizit0'] = i['p3listvizit0'].lstrip()
                i['p3listvizit0'] = i['p3listvizit0'].splitlines()
                vizit0list.append(i['p3listvizit0'])
        vizit0list2 = []
        for i in vizit0list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                vizit0list2.append(i3)

        vizit100 = Tablegameday.objects.values_list('p3listvizit100').filter(p3date=p3dat)
        vizit100list2 = []
        vizit100list22 = []
        for i in vizit100:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.split(',')
                vizit100list22.append(i3)
        for i in vizit100list22:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                vizit100list2.append(i3)

        vizit75 = Tablegameday.objects.values('p3listvizit75').filter(p3date=p3dat)
        vizit75list = []
        for i in vizit75:
            if i['p3listvizit75'] not in vizit75list:
                i['p3listvizit75'] = i['p3listvizit75'].replace(',', '\n')
                i['p3listvizit75'] = i['p3listvizit75'].rstrip()
                i['p3listvizit75'] = i['p3listvizit75'].lstrip()
                i['p3listvizit75'] = i['p3listvizit75'].splitlines()
                vizit75list.append(i['p3listvizit75'])
        vizit75list2 = []
        for i in vizit75list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                vizit75list2.append(i3)

        vizit50 = Tablegameday.objects.values('p3listvizit50').filter(p3date=p3dat)
        vizit50list = []
        for i in vizit50:
            if i['p3listvizit50'] not in vizit50list:
                i['p3listvizit50'] = i['p3listvizit50'].replace(',', '\n')
                i['p3listvizit50'] = i['p3listvizit50'].rstrip()
                i['p3listvizit50'] = i['p3listvizit50'].lstrip()
                i['p3listvizit50'] = i['p3listvizit50'].splitlines()
                vizit50list.append(i['p3listvizit50'])
        vizit50list2 = []
        for i in vizit50list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                vizit50list2.append(i3)

        vizit25 = Tablegameday.objects.values('p3listvizit25').filter(p3date=p3dat)
        vizit25list = []
        for i in vizit25:
            if i['p3listvizit25'] not in vizit25list:
                i['p3listvizit25'] = i['p3listvizit25'].replace(',', '\n')
                i['p3listvizit25'] = i['p3listvizit25'].rstrip()
                i['p3listvizit25'] = i['p3listvizit25'].lstrip()
                i['p3listvizit25'] = i['p3listvizit25'].splitlines()
                vizit25list.append(i['p3listvizit25'])
        vizit25list2 = []
        for i in vizit25list:
            for i2 in i:
                i3 = i2.rstrip().lstrip()
                i3 = i3.replace(',', '')
                vizit25list2.append(i3)

        for i in list(ptsz):
            for ii in pts:
                if i == ii:
                    # pts[ii].append(ptsz[i])
                    # ptsz[i] = pts[ii]
                    ptsz[i]= str(ptsz[i]) + '............' + str(pts[ii])
        ptszitog.append(ptsz)

    trotowtime2 = Tablegameday.objects.values('p3time', 'p3status', 'p3teamviz', 'p3teamhome', 'tvizwl',
                                                   'thomwl', 'p3status2').filter(p3date=p3dat)  #дописать status2
    el22 = []
    el3 = []
    strr2 = []
    qq2 = []
    vr2 = 0
    el22v = {}
    el4 = []

    el6 = []
    for x in trotowtime2:
        # qq2 = str(ptszitog[vr])#.replace('],', '<br>').replace('{', '').replace(']', '').replace('[', '').replace('}',
        # '')  # + sp2[x].values())
        el22.append(x)
        el22.append(ptszitog[vr2])
        el22v.update(x)
        el22v.update(ptszitog[vr2])
        el4.append(el22v)

        el6.append(ptszitog[vr2])
        el22v = {}
        vr2 += 1
        strr2 = []

    iel =0
    el2 = list(el2)
    # for i in el2:
    #     #i = list(i)
    #     if iel > 0 and iel % 2 == 1:
    #         el3.append(i)
    #         el3.append(el22[iel])
    #         print(iel, el2[iel] )
    #     else :
    #         el3.append(i)
    #     #el3[iel] = i
    #     iel +=1

    for i in el2:
        #i = list(i)
        if iel > 0 and iel % 2 == 1:
            el3.append(i)
            el3.append(el22[iel-1])
            el3.append(el22[iel])

        else :
            el3.append(i)
        #el3[iel] = i
        iel +=1
    dt = 1
    p3_t = 'p3teamviz'
    p_el5 = el5
    kalendar(dt,p3_t, p_el5)
    dt = 2
    kalendar(dt,p3_t, p_el5 )
    dt = 3
    kalendar(dt,p3_t, p_el5)
    # dt = 4
    # kalendar(dt,p3_t, p_el5)
    dt = 1
    p3_t = 'p3teamhome'
    p_el5 = el4
    kalendar(dt, p3_t, p_el5)
    dt = 2
    kalendar(dt, p3_t, p_el5)
    dt = 3
    kalendar(dt, p3_t, p_el5)
    # dt = 4
    # kalendar(dt, p3_t, p_el5)

    # kalendar(dt, p3_t, p_el5)



    slovar = {'trotow': trotow,
              'sppl': sppl,
              'indpl': indpl,
              'sppl2': sppl2,
              'sppl4': sppl4,
              'rez2': rez2,
              'irez2': irez2,
              'sp2': sp2,
              'sp3': sp3,
              'lll': lll,
              'ds': ds,
              'el': el,
              'el2': el2,
              'el22': el22,
              'el22v': el22v,
              'el3': el3,
              'el4': el4,
              'el5': el5,
              'el6': el6,
              'l': l,
              # 'iz': iz,
              'itog': itog,
              'trotowtime': trotowtime,
              'trotowtime2': trotowtime2,
              'sttr3': sttr3,
              'menu': menu,

              'zaprosbd' :zaprosbd,
              'zaprosbdnew' :zaprosbdnew,
              'pts':pts,
              'ptsz': ptsz,
              'ptsl': ptsl,
              'com':com,
              'home0':home0,
              'home0list2':home0list2,
              'home100list2': home100list2,
              'home75list2': home75list2,
              'home50list2': home50list2,
              'home25list2': home25list2,

              'home100list': home100list,
              'vizit100': vizit100,
              'vizit100list2': vizit100list2,
              'vizit75list2': vizit75list2,
              'vizit50list2': vizit50list2,
              'vizit25list2': vizit25list2,
              'vizit0list2':vizit0list2,
              'ptszitog': ptszitog,
              #'kalendarbd':kalendarbd,
              'v':v,
              'title': 'O Saite',
              'title': 'Glavna stranica'
              }
    return render(request,'basket/index.html',context=slovar)

def base(request):
    return render(request,'basket/base.html',{ })

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f'<h1>Страница прилож  баскет</h1>{catid}')

def pageNotFound(request, exception):
    print(request.GET)
    return HttpResponseNotFound('<h1>404 errorrr</h1>')

    # for x in trotowtime:
    #     str.append(sp2[vr])
    #     el.append(x)
    #     el.append(str)
    #     vr+= 1
    #     print(str)
    #     print(el)
    #     str=[]