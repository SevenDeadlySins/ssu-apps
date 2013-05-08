# project wide urls
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
# from django.core.urlresolvers import reverse

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.contrib import admin
admin.autodiscover()
# import settings

# import your urls from each app here, as needed
import key_control.urls
from key_control.forms import CrispyAuthenticationForm

urlpatterns = patterns('',

    # urls specific to this app
    url(r'^$', RedirectView.as_view(url='http://www.sonoma.edu/')),
    url(r'^key_control/', include(key_control.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # catch all, redirect to key_control home view
    # url(r'.*', RedirectView.as_view(url='/key_control/home')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'authentication_form': CrispyAuthenticationForm}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
)
