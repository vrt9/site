{% extends 'basket/base.html' %}
{% load static %}
{% block css_additional%}
<link rel="stylesheet" href="{% static 'basket/css/index.css'   %}">
{% endblock   %}
{% block content %}
<!--<div style="width: 15em;border: 1px solid #333; padding: 1px ; display: flex; flex-wrap: nowrap; ">-->
<!--</div>--><br>
{% for ttt in kalendarbd %}
{{ttt}}<br><br>

{% endfor %}<br><br>

{% for ttt in el5 %}
{{ttt}}<br><br>

{% endfor %}<br><br>
{{klnd}}
<div class="boxb">
<div class="col-md-6">
        {% for ttt in el4 %}
      <div class="box"><div class="boxin">
          <div class="box1">  <br>{{ttt.p3time}}   <br> {{ttt.p3teamhome }} {{ttt.thomwl }} <br>
                {{ttt.p3status2}} <br><br> </div>
                {% for tt, k in ttt.items %}
               {% if forloop.counter0 > 5 %}  <span style="background:{% if tt in  home0list2 %}#ffdcdc{% elif tt in  home100list2  %}#9af78f
               {% elif tt in  home75list2  %}#d7f5d3 {% elif tt in  home50list2  %}#e8f9e6 {% elif tt in  home25list2  %}#dfdfdf{% else  %}none{% endif %}">
                    <div class="boxz">{{tt |cut:'p3time' |cut:'p3status2' |cut:'p3teamviz' |cut:'p3teamhome' |cut:'tvizwl' |cut:'thomwl'  }}</div>
                 {{k |cut:'['  |cut:']'   |slice:":66" |cut:'Expected Lineup' |cut:'Confirmed Lineup' }}<br></span>
               {% endif %}   {% endfor %}</div>  </div>  <br><br>
   {% endfor %}</div>

    <div class="col-md-6">
        {% for ttt in el5 %}
      <div class="box"><div class="boxin">
          <div class="box1"> <br> {{ttt.p3time}}   <br> {{ttt.p3teamviz }} {{ttt.tvizwl }} <br>
                {{ttt.p3status}} <br><br> </div>
                {% for tt, k in ttt.items %}
                   {% if forloop.counter0 > 5  and tt != 'klnd' %}  <span style="background:{% if tt in  vizit0list2 %}#ffdcdc{% elif tt in  vizit100list2  %}#9af78f
                   {% elif tt in  vizit75list2  %}#d7f5d3 {% elif tt in  vizit50list2  %}#e8f9e6 {% elif tt in  vizit25list2  %}#dfdfdf{% else  %}none{% endif %}">
                    {% if tt == 1 or  tt == 2 or tt == 3 or tt == 4 or tt == 5 %}
<!--                      <div class="kalend"> {{k |cut:'(' |cut:')'}}</div>-->
             {% else  %}
                      <div class="boxz">
                        {{tt |cut:'p3time' |cut:'p3status2' |cut:'p3teamviz' |cut:'p3teamhome' |cut:'tvizwl' |cut:'thomwl'   }}</div>
                        {{k |cut:'['  |cut:']'  |slice:":66" |cut:'Expected Lineup' |cut:'Confirmed Lineup'}}<br></span>{% endif %} {% endif %}


                {% endfor %}<br><br><br>
      </div>
          <div class="kalend">
             {% if ttt.1 %} {{ttt.1 }} <br>{% endif %}
             {% if ttt.2 %} {{ttt.2 }} <br>{% endif %}
             {% if ttt.3 %} {{ttt.3 }} <br>{% endif %}
              {% if ttt.4 %} {{ttt.4 }} <br>{% endif %}
          </div>

      </div><br><br>

   {% endfor %}</div>
</div>




{% endblock %}