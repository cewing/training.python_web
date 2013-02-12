from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from polls.models import Poll, Choice


def vote_view(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == "POST":
        try:
            choice = poll.choice_set.get(pk=request.POST.get('choice', 0))
        except Choice.DoesNotExist:
            msg = "Ooops, pick a choice that exists, please"
            messages.add_message(request, messages.ERROR, msg)
            url = reverse('poll_detail', args=[pk, ])
        else:
            choice.votes += 1
            choice.save()
            messages.add_message(request, messages.INFO,
                                 "You voted for %s" % choice)
            url = reverse('poll_result', args=[pk])
    else:
        url = reverse('poll_detail', args=[pk, ])

    return HttpResponseRedirect(url)