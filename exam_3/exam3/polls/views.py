from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# Create your views here.
from django.http import HttpResponse
from .models import Question, Product
import datetime

def index(request):
    # 모델클래스 Question을 가져온다. (pub_date 내림차순으로)
    return render(request,'polls/example.html')
    # latest_question_list = Question.objects.order_by('-pub_date')[:3]
    # return render(request, 'polls/index.html',{'latest_question_list' : latest_question_list})

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    q = Question.objects.all()
    return render(request, 'polls/detail.html', {'question' : q})

def results(request, question_id): #question_id를 파라미터로 받는다.
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        # POST form에서 'choice' name 값을 갖는 input의 value 값을 가져온다.
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id = question.id)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def product_create(request):
    register_time = request.POST.get('register_time')[0:10]
    spk = request.POST.get('spk')
    ink = request.POST.get('ink')
    ink_color = request.POST.get('ink_color')
    toner = request.POST.get('toner')
    toner_color = request.POST.get('toner_color')
    etc = request.POST.get('etc')
    quantity = request.POST.get('quantity')


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
    if printer:
        color = colors[selected_printer[printer]]
    if spk and register_time and printer and color and quantity:
        prod_other = Product.objects.filter(name_product = printer, color_product = color, register_date__range=[register_time,datetime.date(2099, 9, 30)])
        if prod_other:
            for p in prod_other:
                print(p)
                if spk=="in":
                    p.stock += quantity
                else:
                    p.stock -= quantity
                if p.stock==0:
                    p.delete()
                else:
                    p.save()
        try:
            prod = Product.objects.get(name_product = printer, color_product = color,register_date__range=[register_time,register_time])
        except:
            p = Product(name_product = printer, color_product = color, stock = quantity, register_date = register_time)
            p.save()

        products = Product.objects.filter(register_date__range=[datetime.date(1900,1,1),register_time]).order_by('-register_date')
        prod = {}
        for p in products:
            print(p,p.stock,p.register_date,sep=" : ")
            if not prod.get(p.name_product):
                prod[p.name_product]=p
        
        for key, value in prod.items():
            print(key,"  ",value.stock,sep=" ")

        return render(request,'polls/product_detail.html',{"prod":prod})

    
    return redirect('polls:index')