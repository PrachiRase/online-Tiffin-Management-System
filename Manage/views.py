from django.shortcuts import render, HttpResponse, redirect
from .models import Contact, Menu, Orders, Payment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')
    #return HttpResponse('This is Home') 

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        #print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form Correctly!!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully!!")
    return render(request, 'contact.html')
    #return HttpResponse('This is contact') 
#function closed
def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This is about') 

def handleSignup(request):
    if request.method == 'POST':
        #Get Parameters
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['semail']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        #Authentications
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        #creating user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')    

def handleLogin(request):
     if request.method == 'POST':
        #Get Parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password= loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('handlecustdets')
        else:
            messages.error(request, "Invalid Credentials, try again")
            return redirect('home')
    
     return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('home')

def handleforgotpass(request):
    if request.method == 'POST':
        em = request.POST['emailpass']

        reg = authenticate(emailaddress = em,)

        if reg is not None:
            login(request, reg)
            messages.success(request, "Password Updated successfully..!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, try again")
            return redirect('forgotpass')

    return render(request, 'forgotpass.html')
    
def handlecustdets(request):
    return render(request, 'custdets.html')

def handleeditprofile(request):
    if request.method == 'POST':
        #Get parameters
        fnam = request.POST['f_name']
        lnam = request.POST['l_name']
        ema = request.POST['e_mail']
        print(fnam,lnam,ema)
        #User.objects.first_name = 'fnam'
        #User.objects.last_name = 'lnam'
        #User.objects.email = 'ema'
        #User.save(update_fields=['first_name','last_name','email'])
        #messages.success(request, "Your profile has been successfully updated")
        #return redirect('custdets')
    else:
        return render (request,'editprofile.html')

def handleadditem(request):
    menu = Menu.objects.all()
    return render(request, 'additem.html',{'menu': menu})

def handleorderdets(request):
    order = Orders.objects.all()
    return render(request, 'orderdets.html',{'order':order})

def handleuserdets(request):
    uorder = Orders.objects.all()
    return render(request, 'userdets.html',{'uorder':uorder})

def handlemodify(request,itemid):
    itemobject = Menu.objects.filter(mid=itemid)
    context = {'itemobject':itemobject}
    return render(request, 'modify.html',context)

def handlemodified(request,itemid):
    itemobject = Menu.objects.filter(mid=itemid)[0]
    food_name = request.POST['food_name']
    veg = request.POST['veg']
    price = request.POST['price']
    name = request.POST['name']
    desc = request.POST['desc']

    itemobject.mtitle = food_name
    itemobject.mtype = veg
    itemobject.mprice = price
    itemobject.mname = name
    itemobject.mdesc = desc

    itemobject.save()

    return redirect('handleadditem')

def handledelete(request,itemid):
    itemobject = Menu.objects.filter(mid=itemid).delete()
    return redirect(request.META['HTTP_REFERER'])

def handlesidenav(request):
    if  request.user.is_authenticated:
        users = User.objects.all()
        user =  request.user
        #method for using full name
        first_name = user.get_first_name()
        last_name = user.get_last_name()
        email = user.get_email()
        
        return render(request,'sidenav.html',{'users': users,
        'first_name':first_name,'last_name':last_name, 'email':email})
    else:
        return redirect ('custdets')

def handlesidenav1(request):
    return render(request, 'sidenav1.html') 

def handleorder(request):
    if request.user.is_authenticated:
        ouser = User.objects.all()
        orderdate = datetime.datetime.now()
        menus = Menu.objects.all()
    
    if request.method=='POST':
        items_json = request.POST.get('itemsjson','')
        amount = request.POST.get('amount','')
        cname = request.POST.get('cname','')
        cemail = request.POST.get('cemail','')
        address = request.POST.get('address','')
        print(items_json, cname, cemail, address)

        #if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
        #    messages.error(request, "please fill the form Correctly!!")
        #else:
        order = Orders(items_json=items_json, amount=amount, cname=cname, cemail=cemail, address=address)
        order.save()
        messages.success(request, "Your Order has been sent successfully!!")
        thank = True
        id = order.order_id
        return render(request,'order.html',{'thank':thank,'id':id})
    return render(request,'order.html',{'ouser':ouser,'orderdate':orderdate,'menus':menus})

# def handlemenu(request):
    if request.method=='POST':
        mtitle = request.POST['mtitle']
        mtype = request.POST['mtype']
        mprice = request.POST['mprice']
        #mimgs = request.POST.get['mimgs',False]
        mdesc = request.POST['mdesc']
        print(mtitle, mtype, mprice, mdesc)

        if len(mtitle)<3 or len(mprice)<1:
            messages.error(request, "please fill the form Correctly!!")
        else:
            menu = Menu(mtitle=mtitle, mtype=mtype, mprice=mprice, mdesc=mdesc)
            Menu.save()
            messages.success(request, "Your Menu has been added successfully!!")
    return render(request, 'menu.html')

def handlepay(request):
    pay = Orders.objects.all()
    if request.method=='POST':
        cardowner = request.POST['cowner']
        cardnumber = request.POST['cnum']
        month = request.POST['month']
        year = request.POST['year']
        cvv = request.POST['cvv']
        payment = Payment(cardowner=cardowner, cardnumber=cardnumber, month=month, year=year, cvv=cvv)
        payment.save()
        messages.success(request, "Your Payment has done successfully!!")
    return render(request, 'payment.html',{'pay':pay})
    
def handlemenucard(request):
    men = Menu.objects.all()
    return render(request, 'menucard.html',{'men':men})