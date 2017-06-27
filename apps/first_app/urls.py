from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login$', views.login, name ='login'),
    url(r'^register$', views.register, name ='register'),
    url(r'^travels$', views.travels, name='travels'),
    url(r'^travels/add$', views.add_plan, name = 'add_plan'),

]
