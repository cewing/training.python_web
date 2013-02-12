from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    ordering = ('choice', )


class PollAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'question',
                    'published_today')
    list_filter = ('pub_date', )
    ordering = ('pub_date', )
    inlines = (ChoiceInline, )


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
