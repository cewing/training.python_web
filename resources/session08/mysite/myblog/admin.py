from django.contrib import admin
from django.core.urlresolvers import reverse
from myblog.models import Post, Category


class CategoryInlineAdmin(admin.TabularInline):
    model = Category.posts.through
    extra = 1
    verbose_name = "Category"
    verbose_name_plural = "Categories"


class PostAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'created_date', 'modified_date',
                    'published_date', 'author_link')
    readonly_fields = ('created_date', 'modified_date')
    inlines = [CategoryInlineAdmin, ]

    def author_link(self, post):
        url = reverse('admin:auth_user_change', args=(post.id,))
        name = post.author_name()
        return '<a href="%s">%s</a>' % (url, name)
    author_link.allow_tags = True

    def get_readonly_fields(self, request, obj=None):
        fields = ()
        if obj is not None:
            fields = self.readonly_fields
        return fields


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
