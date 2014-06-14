from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'blog.views.logout_view'),
    url(r'^register/$', 'blog.views.register_user'),
    url(r'^reg_success', 'blog.views.register_success'),

    #post
    url(r'^add_post$','blog.views.add_post',name='blog_add_post'),
    url(r'^post/(?P<slug>[-\w]+)$','blog.views.view_post',name='blog_post_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
