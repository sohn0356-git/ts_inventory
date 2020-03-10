from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm_P
from user.decorator import login_required
from django.utils.decorators import method_decorator
from .models import Order
from django.db import transaction
from product_p.models import Product_p
from user.models import User
# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm_P
    success_url = '/product_p/'
    
    def form_valid(self,form):
        prod = Product_p.objects.get(pk=form.data.get('product'))
        with transaction.atomic():
            order = Order(quantity=form.data.get('quantity'),product = prod,
            user = User.objects.get(userid=User.objects.get(userid = self.request.session.get('user'))))
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product_p/'+str(int(form.data.get('product'))))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__useremail = self.request.session.get('user'))
        return queryset
