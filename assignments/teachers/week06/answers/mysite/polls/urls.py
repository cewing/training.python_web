from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.http import HttpResponse

from polls.models import Poll


def stub(request, *args, **kwargs):
    return HttpResponse('stub view', mimetype="text/plain")


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='polls',
            template_name="polls/list.html"
        ),
        name="poll_list"),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name="polls/detail.html"
        ),
        name="poll_detail"),
    url(r'^(?P<pk>\d+)/vote/$',
        'polls.views.vote_view',
        name="poll_vote"),
    url(r'^(?P<pk>\d+)/result/$',
        DetailView.as_view(
            model=Poll,
            template_name="polls/result.html"),
        name="poll_result")
)