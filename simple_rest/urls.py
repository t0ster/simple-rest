from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from simple_rest.core import views

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^revoke-access/$', 'simple_rest.core.views.revoke_access'),

    url(r'^admin/', include(admin.site.urls)),
)
