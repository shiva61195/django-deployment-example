from django.conf.urls import url
from tempapp import views

#Template tagging;
app_name = 'tempapp'

urlpatterns = [
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other'),
]
