from django.conf.urls.defaults import *
from denver.mobileviews import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^denver/', include('denver.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    (r'^$', views.mobile_view, {}, "mobile_view"),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
