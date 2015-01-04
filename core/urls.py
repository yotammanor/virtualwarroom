from django.conf.urls import patterns, include, url
from core import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'virtualwarroom.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', views.HomePageView.as_view(), name='homepage'),
)
