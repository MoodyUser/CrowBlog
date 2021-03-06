from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^add-new/$', 'blog.views.add_new_post', name="add_new_post"),
    url(r'^contact-us/$', 'blog.views.contact_us', name="contact"),

    url(r'^(\d+)/$', 'blog.views.single_post', name='post'),
    url(r'^(\d+)/edit/$', 'blog.views.update_post', name='edit_post'),
    url(r'^([a-zA-Z][-\w]*)/$', 'blog.views.single_post_by_slug', name='post_by_slug'),
    # url(r'^blog/', include('blog.urls')),

)
