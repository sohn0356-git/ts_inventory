from django.shortcuts import render, get_object_or_404
from django.views import generic
# Create your views here.
from django.http import HttpResponse
from .models import Question, Product_p
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
    quantity = int(request.POST.get('quantity'))

    #-------------debug------------------------#
    # print("register_time : "+ register_time)
    # print("spk : "+spk)
    # print("ink : "+ink)
    # print("toner : "+toner)
    # print("toner_color : "+toner_color)
    # print("etc : "+etc)
    # print("quantity : "+quantity)

    if register_time and spk and ink and ink_color and toner and toner_color and etc and quantity:
        try:
            prod = Product_p.objects.filter(name_printer = ink, color_printer = ink_color, name_toner = toner, color_toner = toner_color,register_date__range=[register_time,datetime.date(2099, 9, 30)])
        except Product_p.DoesNotExist:
            prod = Product_p(name_printer = ink, color_printer = ink_color, name_toner = toner,
        color_toner = toner_color, category_toner = etc, stock = quantity, register_date = register_time) 
            prod.save()
            return render(request,'polls/product_detail.html',{'prod':prod})
        for p in prod:
            if spk=="in":
                p.stock += quantity
            else:
                p.stock -= quantity 
            if p.stock==0:
                p.delete()
            else:
                p.save()

    return render(request,'polls/product_detail.html',{'prod':prod})