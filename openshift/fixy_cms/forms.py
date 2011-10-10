from fixy_cms.models import *
from django.forms import *
from tekextensions.widgets import SelectWithPopUp
from django.utils.translation import ugettext as _
from django.conf import settings
import os

post_template_dir=os.path.join(settings.TEMPLATE_DIR, 'post/display_templates')
class TemplateForm(ModelForm):

    str_name=CharField(label=_('Title'),widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    def clean_str_name(self):
        str_name = self.cleaned_data['str_name']
        template_dir=os.path.join(post_template_dir,str_name)
        if os.path.exists(template_dir):
            raise forms.ValidationError(_("Template already exists"))
        return str_name

    class Meta:
        model=PostTemplate 
    

class PostForm(ModelForm):

    str_post_title=CharField(label=_('Title'),widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_post_summary=CharField(label=_('Summary'),widget=forms.Textarea(attrs={'cols':'70','rows':'2','class':'text95'}))
    category=ModelMultipleChoiceField(queryset=Category.objects.all(),required=False)
    str_post_status=ChoiceField(label=_("Status"),choices=Post.POST_STATUS,required=True)
    str_comment_status=BooleanField(label=_("Are comment Allowed?"),required=False)
    str_post_content=CharField(label=_('Content'),widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95 mceEditor'}))

    #category = ModelChoiceField(Category.objects, widget=SelectWithPopUp)
    class Meta:
        model=Post
        fields = ('str_post_title','str_slug', 'str_post_summary','str_post_content','str_post_status','str_comment_status','template')
