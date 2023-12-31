from django.shortcuts import render,redirect
from happ.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/adlogin/')
def adhome(request):
    return render(request,'happ/adhome.html')

@login_required(login_url='/adlogin/')
def addisplay(request):
    d=Addproduct.objects.all()
    context={
        'd':d
    }
    return render(request,'happ/addisplay.html',context)


@login_required(login_url='/adlogin/')
def addproduct(request):
    if request.method=="POST":
        no=request.POST.get('no')
        name=request.POST.get('name')
        image=request.FILES.get('image')
        price=request.POST.get('price')
        details=request.POST.get('details')
        d=Addproduct(no=no,name=name,image=image,price=price,details=details)
        d.save()

    
    return render(request,'happ/adproduct.html')


@login_required(login_url='/adlogin/')
def update(request,id):
    d=Addproduct.objects.get(id=id)
    context={
        'd':d
    }
    if request.method=="POST":
        d.no=request.POST.get('no')
        name=request.POST.get('name')
        d.image=request.FILES.get('image')
        d.price=request.POST.get('price')
        d.details=request.POST.get('details')
        d.save()
        return redirect('/addisplay/')
    return  render(request,'happ/update.html',context)


@login_required(login_url='/adlogin/')
def delete(request,id):
    d=Addproduct.objects.get(id=id)
    d.delete()
    return redirect("/addisplay/")




def adregister(request):
    d=UserCreationForm()
    context={
        'd':d
    }
    if request.method=="POST":
        d=UserCreationForm(request.POST)
        if d.is_valid():
            d.save()
            return redirect('/adlogin/')
    return render(request,'happ/adregister.html',context)

def main(request):
    return render(request,'happ/main.html')


@login_required(login_url="/ulogin/")
def uregister(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        copassword=request.POST.get('copassword')
        d=register(name=name,password=password,copassword=copassword)
    
        if password==copassword:
        
            d.save()
            return redirect('/ulogin/')
        else:
            return redirect('/uregister/')
    
           


    return render(request,'happ/uregister.html')

def ulogin(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        n=register.objects.values('name')
        p=register.objects.values('password')
        for i in range(len(n)):
            if name in n[i]["name"] and password in p[i]["password"]:
                return redirect("/uhome/")
            
    return render(request,'happ/ulogin.html')


@login_required(login_url="/ulogin/")
def uhome(request):
    return render(request,'happ/uhome.html')

def uorders(request):
    return render(request,'happ/orders.html')


def uitem(request):
    d=Addproduct.objects.all()
    context={
        'd':d
    }
    return render(request,'happ/uitem.html',context)
    
def user(request,id):
    d=Addproduct.objects.get(id=id)
    u=User(no=d.no,name=d.name,image=d.image,price=d.price,details=d.details)
    u.save()
    return redirect('/uitem/')
    


def udelete(request,id):
    u=User.objects.get(id=id)
    u.delete()
    return redirect('/uorderitem/')


def uorderitem(request):
    u=User.objects.all()
    context={
        'u':u
    }
    return render(request,'happ/uorderitem.html',context)

def ureview(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        comment=request.POST.get("comment")
        d=review(n=name,email=email,comment=comment)
        d.save()

    return render(request,'happ/ureview.html')

def adreview(request):
    d=review.objects.all()
    context={
        'd':d
    }
    return render(request,'happ/adreview.html',context)

def addelete(request,id):
    d=review.objects.get(id=id)
    d.delete()
    return redirect('/adreview/')

import io
from rest_framework.parsers import JSONParser
from django.views import View
from .serializer import *
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class Product(View):
    def get(self,request,*args,**kwargs):
        if request.method=="GET":
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id=pythondata.get('no',None)
            if id is not None:
                stu=Addproduct.objects.get(no=id)
                ser=Productser(stu)
                # json_data=JSONRenderer().render(ser)
                return JsonResponse(ser.data,safe=False)
            stu=Addproduct.objects.all()
            ser=Productser(stu,many=True)
            # json_data=JSONRenderer().render(ser.data)
            return JsonResponse(ser.data,safe=False)
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            ser=Productser(data=pythondata)
            if ser.is_valid():
                ser.save()
                msg={'msg':"created!"}
                # json_data=JSONRenderer().render(msg)
                return JsonResponse(msg,safe=False)
            return JsonResponse(ser.errors)
    def put(self,request,*args,**kwargs):
        if request.method=="PUT":
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id=pythondata.get('no')
            pro=Addproduct.objects.get(no=id)
            ser=Productser(pro,data=pythondata,partial=True)
            if ser.is_valid():
                ser.save()
                msg={'msg':'updated!'}
                return JsonResponse(msg,safe=False)
            return JsonResponse(ser.errors)
    def delete(self,request,*args,**kwargs):
        if request.method=="DELETE":
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            no=pythondata.get('no')
            pro=Addproduct.objects.get(no=no)
            pro.delete()
            return f"deleted!"


