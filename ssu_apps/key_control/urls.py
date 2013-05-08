# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from .views import PositionListView, PositionDetailView, PositionFormView, CreateSequenceView, UserTypeView, KeyTypeView, KeyIssueView, KeyReturnView, KeyReturnResultsView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^issue/$', KeyIssueView.as_view()),
    url(r'^return/$', KeyReturnView.as_view()),
    url(r'^return/results/$', KeyReturnResultsView.as_view()),
    url(r'^position/$', PositionListView.as_view()),
    url(r'^position/(?P<pk>\d*)/$', PositionDetailView.as_view()),
    url(r'^position/(?P<pk>\d*)/createseq/$', CreateSequenceView.as_view()),
    url(r'^position/add/$', PositionFormView.as_view()),
    url(r'^usertypes/$', UserTypeView.as_view()),
    url(r'^keytypes/$', KeyTypeView.as_view()),
)
