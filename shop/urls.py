from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

app_name="shop"

urlpatterns = [
    url(r'^$', views.details_list, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'shop:login'}, name='logout'),
    url(r'^new_detail/$', views.new_detail, name='new_detail'),
    url(r'^audi_a8_d2_3_3/$', views.audi_a8_d2_3_3, name='audi_a8_d2_3_3'),
    url(r'^audi_a8_d2_3_7/$', views.audi_a8_d2_3_7, name='audi_a8_d2_3_7'),
    url(r'^audi_a8_d2_4_2/$', views.audi_a8_d2_4_2, name='audi_a8_d2_4_2'),
    url(r'^audi_a8_d3_3_0/$', views.audi_a8_d3_3_0, name='audi_a8_d3_3_0'),
    url(r'^audi_a8_d3_3_7/$', views.audi_a8_d3_3_7, name='audi_a8_d3_3_7'),
    url(r'^audi_a8_d3_4_2/$', views.audi_a8_d3_4_2, name='audi_a8_d3_4_2'),
    url(r'^mitsubishi_3_2/$', views.mitsubishi_3_2, name='mitsubishi_3_2mitsubishi_3_5'),
    url(r'^mitsubishi_3_5/$', views.mitsubishi_3_5, name='mitsubishi_3_5'),
    url(r'^porshe_cayenne/$', views.porshe_cayenne, name='porshe_cayenne'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_page, name='detail_page'),
    url(r'^search/$', views.detail_search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
