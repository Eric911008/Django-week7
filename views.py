from django.shortcuts import render
from django.http import HttpResponse,Http404
from mysite.models import Product
import random
from datetime import datetime


def carlist(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
                    [
                        {'model':'Fiesta','price':203500},
                        {'model':'Focus','price':605000},
                        {'model':'Mustang','price':900000}
                    ],
                    [
                        {'model':'Fit','price':450000},
                        {'model':'City','price':150000},
                        {'model':'NSX','price':1200000}
                    ],
                    [
                        {'model':'Mazada3','price':329999},
                        {'model':'Mazada5','price':603000},
                        {'model':'Mazada6','price':850000}
                    ]
                ]

    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())

def index(request, tvno=0):
    tv_list = [
        {'name':'東森', 'tvcode':'1CPmsXbPzco'},
        {'name':'民視', 'tvcode':'ylYJSBUgaMA'},
        {'name':'台視', 'tvcode':'pkFoyQoGfeg'},
        {'name':'三立', 'tvcode':'jlldIiGA5bU'}
    ]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "index.html", locals())


def engtv(request, tvno=0):
    tv_list = [
        {'name':'Sky News', 'tvcode':'9Auq9mYxFEE'},
        {'name':'Euro News', 'tvcode':'pykpO5kQJ98'},
        {'name':'India News', 'tvcode':'Xmm3Kr5P1Uw'}
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, "engtv.html", {'tv':tv, "now":now})

def add(request, a=8, b=7):
    return HttpResponse("{}+{}={}".format(a,b,a+b))

def about(request, author_no=0):
    quotes = ["AAA","BBB","CCC","DDD","EEE"]
    quote = random.choice(quotes)
    author_no = author_no
    return render(request, "about.html", locals())


def listing(request, uid='', name='', age=0):
#    html = '''
#<!DOCTYPE html>
#<html>
#<head>
#    <meta charset="utf-8">
#    <title>Mobile</title>
#</head>
#<body>
#<h2>Mobile</h2>
#<table width="400" border=1 bgcolor="#ccffcc">
#    {}
#</table>
#</body>
#</html>
#'''

    products = Product.objects.all()
    tags = '<tr><td>item number</td><td>brand name</td><td>price</td><td>size</td></tr>'

    d = "({}/{}/{})".format(uid, name, age)

    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.sku)
        tags = tags + '<td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.get_size_display())

    return render(request, "list.html", locals())


def disp_detail(request,sku):

    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404("Cannot find the specified item !!!")
    tags = '<tr><td>item number</td><td>{}</td></tr>'.format(p.sku)
    tags += '<tr><td>brand name</td><td>{}</td></tr>'.format(p.name)
    tags += '<tr><td>price</td><td>{}</td></tr>'.format(p.price)
    #return HttpResponse(html.format(p.name, p.name, tags))
    return render(request, "disp_detail.html", locals())
