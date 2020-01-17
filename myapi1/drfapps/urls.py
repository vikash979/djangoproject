from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
#
from django.conf.urls import url
from . import views
app_name = 'drfapps'
urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),


    #path('users/', include('django.contrib.auth.urls')),
]
urlpatterns = [
    # /movie1/
   # url(r'^$', views.index, name='index'),
    url(r'^acti/$', views.acti, name='acti'),
    path("logout_request", views.logout_request, name="logout_request"),
    url(r'^signup/$', views.signup, name='signup'),

    # /movie1/<moviesList_id>/

    # url(r'^getdata', views.getdata ),

    # url(r'^(?P<question_id>[0-9]+)/$' ,views.detail,name='detail'),

]