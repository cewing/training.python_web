from django.conf.urls import patterns, url


urlpatterns = patterns('myblog.views',
    url(r'^$',
        'list_view',
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        'detail_view',
        name="blog_detail"),
    url(r'^add/$',
        'add_view',
        name="add_post"),
)
