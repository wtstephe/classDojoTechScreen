from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'classDojo.views.home', name='home'),
    # url(r'^classDojo/', include('classDojo.foo.urls')),
    #url(r'^matrixPath/', include('matrixPath.urls'))
    url(r'^$', 'views.receiveRequest', name = 'receiveRequest')
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
