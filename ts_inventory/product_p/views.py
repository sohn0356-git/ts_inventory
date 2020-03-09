from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product_p
from user.decorator import login_required, admin_required
from django.utils.decorators import method_decorator
from .forms import RegisterForm
import pandas
#from order.forms import RegisterForm as OrderForm
# Create your views here.

class ProductList(ListView):
    model = Product_p
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product_p/'

    def form_valid(self, form):
        register_date_start=form.data.get('register_date_start')
        register_date_end = form.data.get('register_date_end')
        
        dt_index = pandas.date_range(start=form.data.get('register_date_start'),
        end = form.data.get('register_date_end'),freq='MS')
        dt_list = set(dt_index.strftime("%Y-%m-%d").tolist())
        for i in dt_list:
            product = Product_p(name_printer=form.data.get('name_printer'),
            name_toner=form.data.get('name_toner'),
            category_toner=form.data.get('category_toner'),
            pre_stock=form.data.get('pre_stock'),
            in_stock=form.data.get('in_stock'),
            out_stock=form.data.get('out_stock'),
            out_description=form.data.get('out_description'),
            stock=form.data.get('stock'),
            remark=form.data.get('remark'),
            register_date = i,
            register_date_start=form.data.get('register_date_start'),
            register_date_end = form.data.get('register_date_end'))
            product.save()

        
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product_p.objects.all()
    context_object_name = 'product'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = OrderForm(self.request)
    #     return context

