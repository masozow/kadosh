from django.conf.urls import include, url
from . import views

urlpatterns=[
#urls para loguear
url(r'^$','django.contrib.auth.views.login',
 {'template_name':'kadoshapp/login.html'}, name='login'),

url(r'^$','django.contrib.auth.views.logout_then_login',
 name='logout'),
url(r'', views.ingreso_mercaderia),

]
