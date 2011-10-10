from fixy_cms.models import *
from fixy_cms.forms import *
from fixy_cms.utilities import *
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.conf import settings
import os


 
post_template_dir=os.path.join(settings.TEMPLATE_DIR, 'post_templates')

class PostCategoryInline(admin.TabularInline):
    model=PostCategory
    category = ModelMultipleChoiceField(widget=CheckboxSelectMultiple(),queryset=Category.objects.all(),required=True)
    extra=2


class CommentsInline(admin.TabularInline):
    model=Comments
    extra=0

class PostSpecialFieldInline(admin.TabularInline):
    
    model = PostSpecialField
    extra = 0
class ContentAdmin(admin.ModelAdmin):
    exclude = ('dt_post_date', 'dt_post_date_modified')
class CategoryAdmin(admin.ModelAdmin):
    fields = ('str_name', 'parent')
    #inlines = [PostSpecialFieldInline,PostCategoryInline]
class TemplateAdmin(admin.ModelAdmin):
    form=TemplateForm
    list_display = ('str_name',)
    def save_model(self, request, obj, form, change):
        
        obj.save()
        template_dir=os.path.join(post_template_dir,obj.str_name)
        unzip_file_into_dir(obj.str_file,template_dir)
        


class PostAdmin(admin.ModelAdmin):
    
    form=PostForm
    list_display = ('str_post_title', 'dt_post_date','author','template')
    list_filter = ('dt_post_date','author')
    ordering = ('dt_post_date','author')
    search_fields = ('dt_post_date',)
    #fields=('str_post_title','str_post_summary',)        
    inlines = [PostSpecialFieldInline,CommentsInline]
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    
admin.site.register(PostTemplate,TemplateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
