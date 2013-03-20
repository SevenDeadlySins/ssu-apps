# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from .views import PositionListView, PositionDetailView, PositionFormView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^issue/$', TemplateView.as_view(template_name="keyissue.html")),
    url(r'^position/list/$', PositionListView.as_view()),
    url(r'^position/view/(?P<pk>\d*)/$', PositionDetailView.as_view()),
    url(r'^position/add/$', PositionFormView.as_view())
)
