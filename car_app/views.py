from django.shortcuts import render,redirect
from django.urls import reverse
from car_app.models import Brand, Car_details, Car_sell, Color, Fueltype, call_request
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum

from django.core.paginator import Paginator





# Create your views here.


def index(request):
    details=Car_details.objects.filter().order_by('-id')[:6]
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color
    }
    return render(request,'index.html',context)

def brand(request,id):
    details=Car_details.objects.filter(brand_id=id)
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color,
    }
    return render(request,'brand.html',context)

def car_fulldetails(request,id):
    details=Car_details.objects.get(id=id)
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color
    }
    print(context)
    return render(request,'details.html',context)

def newarival(request):
    details=Car_details.objects.filter().order_by('-id');
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color
    }
    return render(request,'index.html',context)

def carsfull(request):

    detail=Car_details.objects.all()
    brand=Brand.objects.all()
    color=Color.objects.all()
    fuel=Fueltype.objects.all()

    #paginate

    paginator=Paginator(detail,6)
    page_no=request.GET.get('page')
    details=paginator.get_page(page_no)


    context={
        'details':details,
        'brand':brand,
        'color':color,
        'fuel':fuel,
    }
    return render(request,'cars.html',context) 

def topprice(request):
    details=Car_details.objects.filter().order_by('-price');
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color
    }
    return render(request,'index.html',context)
def lowprice(request):
    details=Car_details.objects.filter().order_by('price');
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color
    }
    return render(request,'index.html',context)

def login(request):
    return render(request,'signup.html')

def carsell(request):
    brand=Brand.objects.all()
    color=Color.objects.all()
    fuel=Fueltype.objects.all()
    context={
        'brand':brand,
        'color':color,
        'fuel':fuel
    }
    return render(request,'carsel.html',context)

def signup(request):
    if request.method == 'POST':
        username=request.POST ['username']
        firstname=request.POST ['firstname']
        email=request.POST ['email']
        password=request.POST ['password']
        password2=request.POST ['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'email alredy taken')
                return redirect('login')
            elif User.objects.filter(username=username).exists():
                messages.error(request,'username taken')
                return redirect('login')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
            
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                messages.success(request,'Your account create successfully')
                return redirect('login')
        else:
            messages.error(request,'password not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')

def signin(request):
    if request.method=='POST':
        username=request.POST ['username']
        password=request.POST ['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, f'Login successfull,welcome {username}')
            return redirect('index')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    return render(request,'signup.html')


def addcar(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            seller_name=request.POST ['seller_name']
            number=request.POST ['number']
            email=request.POST ['email']
            car_name=request.POST ['car_name']
            car_price=request.POST ['car_price']
            brand_name=request.POST['brands']
            fuel_type=request.POST ['fuel_type']
            color=request.POST ['color']
            image1=request.POST ['image1']
            image2=request.POST ['image2']
            year=request.POST ['year']
            kilometer=request.POST ['kilometer']
            owners=request.POST ['owners']
            features=request.POST ['features']


            select_brand=Brand.objects.get(brand_name=brand_name)
            select_fuel=Fueltype.objects.get(fuel=fuel_type)
            select_color=Color.objects.get(color_name=color)

            carsell_details=Car_sell(owner_user=request.user,seller_name=seller_name,phone=number,email=email,car_name=car_name,brand=select_brand,fuel_type=select_fuel,price=car_price,image1=image1,image2=image2,color=select_color,year=year,kilometer=kilometer,owners=owners,features=features)
            carsell_details.save()
            messages.success(request,'details added successfully')
            return redirect('carsell')
    else:
        messages.error(request,'please login')
        return redirect('login')


def callrequest(request):
    if request.method=='POST':
        name=request.POST ['name']
        number=request.POST ['number']
        email=request.POST ['mail']
        message=request.POST ['msg']

        req=call_request(owner_user=request.user,name=name,phone_no=number,email=email,message=message)
        req.save()
        messages.success(request,'Request Send Successfully and we will contact back')
        return redirect('index')
    else:
        return redirect('index')
    
def search(request):
        query = request.GET.get('query')
        detail = Car_details.objects.all().filter(Q(car_name__contains=query) | Q(brand__contains=query))

        context = {
            'detail': detail
        }
        return render(request,'search.html',context)
    

def filtercolor(request,id):
    details=Car_details.objects.filter(color=id)
    brand=Brand.objects.all()
    color=Color.objects.all()
    fuel=Fueltype.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color,
        'fuel':fuel
    }
    return render(request,'cars.html',context)


def filterbrand(request,id):
    details=Car_details.objects.filter(brand_id=id)
    brand=Brand.objects.all()
    color=Color.objects.all()
    fuel=Fueltype.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color,
        'fuel':fuel
    }
    return render(request,'cars.html',context)


def filterfuel(request,id):
    details=Car_details.objects.filter(fuel_type=id)
    brand=Brand.objects.all()
    color=Color.objects.all()
    fuel=Fueltype.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color,
        'fuel':fuel
    }
    return render(request,'cars.html',context)

def filterprice(request,id):
    details=Car_details.objects.filter(price_range=id)
    brand=Brand.objects.all()
    color=Color.objects.all()
    fuel=Fueltype.objects.all()
    context={
        'details':details,
        'brand':brand,
        'color':color,
        'fuel':fuel
    }
    return render(request,'cars.html',context)


