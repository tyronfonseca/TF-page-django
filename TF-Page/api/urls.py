from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import ListView
from . import views
from .models import PagesModel

urlpatterns = [
    url(r'^$',views.GenderNameList.as_view(), name ='index'),
    url(r'^(?P<name>.+)/$',views.GetGenderName.as_view(), name ='get'),
    url(r'^create/$',views.CreateGenderName.as_view(), name ='create'),
    url(r'^(?P<pk>\d+)/delete/$',views.DeleteGenderName.as_view(), name ='delete'),
    url(r'^fb/$',ListView.as_view(queryset=PagesModel.objects.all(),
     template_name="facebook/test.html"))
   ]
urlpatterns = format_suffix_patterns(urlpatterns)