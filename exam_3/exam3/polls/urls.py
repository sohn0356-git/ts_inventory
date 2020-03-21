from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 숫자로 이루어진 question_id를 매개변수로 저장해서 views.py에 넘긴다
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^list/$', views.product_create, name='product_create'),
    url(r'^search/$',views.search, name = 'search'),
    url(r'^login/',views.LoginView.as_view()),
    url(r'^register/',views.RegisterView.as_view()),
]