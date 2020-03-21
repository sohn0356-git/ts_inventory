from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.views import generic
from django.utils.decorators import method_decorator
from user.decorator import login_required, admin_required
# Create your views here.
from django.http import HttpResponse
from .models import Product
import datetime, calendar
from user.models import User

# Create your views here.

# @method_decorator(admin_required, name='dispatch')
def product_create(request):
    user = request.session.get('user')
    if user is None or not user:
        return redirect('/login')
    user = User.objects.get(userid=user)
    if user.level!='admin':
        return redirect('/')
    if request.method=='GET':  
        print("get")
        return render(request,'example.html')

    if request.POST.get('register_time'):
        userid = request.session.get('user')
        user = User.objects.get(userid = userid)
        register_time = request.POST.get('register_time')[0:10]
        spk = request.POST.get('spk')
        ink = request.POST.get('ink')
        ink_color = request.POST.get('ink_color')
        toner = request.POST.get('toner')
        toner_color = request.POST.get('toner_color')
        etc = request.POST.get('etc')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        printer = request.POST.get('printer')
        ink_Choices = request.POST.get('ink_Choices')
        ink1 = request.POST.get('ink1')
        selected_printer = {"EPSON L7160":0,"HP Officejet Pro 8600":1,"EPSON WF-2521":2,
                            "HP Officejet Pro 8720":3,"EPSON(홍보팀)":4,"ML-8851N":5,
                            "SL-C486FW":6,"SL-C473FW":7,"SL-M4530ND":8,"SL-M2950ND":9,
                            "폐토너통":10,"이미징 유닛":11}
        colors = []
        colors.append(request.POST.get('color1'))
        colors.append(request.POST.get('color2'))
        colors.append(request.POST.get('color3'))
        colors.append(request.POST.get('color4'))
        colors.append(request.POST.get('color5'))
        colors.append(request.POST.get('color6'))
        colors.append(request.POST.get('color7'))
        colors.append(request.POST.get('color8'))
        colors.append(request.POST.get('color9'))
        colors.append(request.POST.get('color10'))
        colors.append(request.POST.get('color11'))
        colors.append(request.POST.get('color12'))
        
        
            
        if quantity!='':
            quantity = int(quantity)
            print("quantity : "+str(quantity))

        #-------------debug------------------------#
        # for idx, c in enumerate(colors):
        #     if c:
        #         if idx==selected_printer[printer]:
        #             print("selected item is ",end=" : ")

        #         print(idx+1,c)
        
        # if register_time:
        #     print("register_time : "+ register_time)
        # if ink1:
        #     print("ink1 : "+ink1)
        
        # if spk:
        #     print("spk : "+spk)
        # if printer:
        #     print("printer : "+printer)
        # if ink_Choices:
        #     print("ink_Choices : "+ink_Choices)
        # if ink:
        #     print("ink : "+ink)
        # if toner:
        #     print("toner : "+toner)
        # if toner_color:
        #     print("toner_color : "+toner_color)
        # if etc:
        #     print("etc : "+etc)
        print(userid)
        if printer:
            color = colors[selected_printer[printer]]
        if spk and register_time and printer and color and quantity:
            ### 나보다 뒤에 있는 애들 갱신 ###
            prod_next = Product.objects.filter(name_product = printer, color_product = color, register_date__range=[register_time,datetime.date(2099, 9, 30)])
            if prod_next:
                for p in prod_next:
                    if spk=="in":
                        p.stock += quantity
                    else:
                        p.stock -= quantity
                    if p.stock==0:
                        p.delete()
                    else:
                        p.save()
        
            ### 현재 재고량 불러오기 ###
            prod_prev = Product.objects.filter(name_product = printer, color_product = color, register_date__range=[datetime.date(1900,1,1),register_time]).order_by('-register_date')

            ### 내가 최신일 때 == 재고량 0 ###
            if not prod_prev:
                if spk=="in":
                    p = Product(user= user,name_product = printer, color_product = color, in_stock = quantity, out_stock = 0, month_in = 0, month_out = 0, stock = quantity, register_date = register_time)
                    p.save()
                
                ### detail view 넘길 데이터 생성###
                products = Product.objects.filter(register_date__range=[datetime.date(1900,1,1),register_time]).order_by('-register_date')
                prod = {}
                prod_list = []
                for p in products:
                    if not prod.get(p.name_product):
                        prod[p.name_product]=p
                
                for key, value in prod.items():
                    prod_list.append(value)
                    print(key,"  ",value.stock,sep=" ")
                return render(request,'product_detail.html',{"prod":prod_list})

            ### 재고가 있었을 때 ###
            if spk=="in":
                cur_stock = prod_prev[0].stock + quantity
                p = Product(user= user,name_product = printer, color_product = color, in_stock = quantity, out_stock = 0,description=description, month_in = 0, month_out = 0, stock = cur_stock, register_date = register_time)
                p.save()
            else:
                cur_stock = prod_prev[0].stock - quantity
                p = Product(user= user,name_product = printer, color_product = color, in_stock = 0, out_stock = quantity,description=description, month_in = 0, month_out = 0, stock = cur_stock, register_date = register_time)
                p.save()
            
            
            
            ### detail view 넘길 데이터 생성###
            products = Product.objects.filter(register_date__range=[datetime.date(1900,1,1),register_time]).order_by('-register_date')
            prod = {}
            prod_list = []
            for p in products:
                print(p,p.stock,p.register_date,sep=" : ")
                if not prod.get(p.name_product):
                    prod[p.name_product]=p
            
            for key, value in prod.items():
                prod_list.append(value)
                print(key,"  ",value.stock,sep=" ")

            return render(request,'product_detail.html',{"prod":prod_list})

    return redirect('product_create')


def search(request):
    user = request.session.get('user')
    if user is None or not user:
        return redirect('/login')

    if request.method=='GET':  
        print("get")
        return render(request,'test.html')

    print("post")
    register_time = ""
    if request.POST.get('register_time'):
        register_time = request.POST.get('register_time')[0:10]  
        print(register_time)
        products = Product.objects.filter(register_date__range=[datetime.date(1900,1,1),register_time]).order_by('-register_date')
        prod = {}
        prod_list = []
        year = register_time[0:4]
        month = register_time[5:7]
        for p in products:
            print(p,p.stock,p.register_date,sep=" : ")
            if not prod.get(p.name_product):
                
                start_date = register_time[0:8]+"01"
                end_date = register_time[0:8]+str(calendar.monthrange(int(year),int(month))[1])
                month_prod = Product.objects.filter(name_product = p.name_product, color_product = p.color_product, register_date__range=[start_date,end_date])
                month_in = 0
                month_out = 0
                month_description = []
                if month_prod:
                    for mp in month_prod:
                        month_in += mp.in_stock
                        month_out += mp.out_stock
                        if mp.description:
                            month_description.append(mp.description)
                p.month_in = month_in
                p.month_out = month_out
                p.description = ', '.join(month_description)
                prod[p.name_product]=p
        
        for key, value in prod.items():
            prod_list.append(value)
            print(key,"  ",value.stock,sep=" ")
        return render(request,'test.html',{"prod":prod_list})
    return render(request,'test.html')