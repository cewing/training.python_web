from django.conf.urls import patterns, url


urlpatterns = patterns('myblog.views',
    url(r'^$',
        'list_view',
        name="blog_index"),
    url(r'^posts/(\d+)/$',
        'detail_view',
        name="blog_detail"),
)
