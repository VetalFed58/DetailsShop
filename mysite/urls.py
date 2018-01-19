from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from shop import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^signup/$', core_views.signup, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
