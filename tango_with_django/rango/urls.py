from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^ajax/$', views.ajax, name='ajax'),
                        # need to add veiw first
                        url(r'^about/$', views.about, name='about'),
                        url(r'^dom/$', views.dom, name='dom'),
                        url(r'^jsexample/$', views.jsexample, name='jsexample'),

)
