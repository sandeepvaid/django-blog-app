from django.urls import re_path as url
from blogger import views
from django.urls import path

urlpatterns = [ 
    url(r'^api/blogger/(?P<user_id>[\w\d\.!@#\$%\^&\*\(\)_\+\{\}\[\]\|\\`~-]+)/$', views.blogger_list),
    url(r'^api/blogger/add$', views.blogger_add),
    url(r'^api/blogger/delete/([0-9]+)$', views.blogger_delete),
    url(r'^api/blogger/update/([0-9]+)$', views.blogger_update),
    url(r'^api/blogger/detail/([0-9]+)$', views.blogger_detail),

]