from django.conf.urls import url
from MyApp import views
app_name = 'MyApp'
urlpatterns = [
    url(r'^about',views.about,name='about'),
    url(r'^careers',views.careers,name='careers')
]
