from models import *
from django.forms import *
from django.utils.translation import ugettext as _



class WebVideoForm(ModelForm):

#    help_text="Use puns liberally",
    str_name=CharField(label=_('Title'),widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_description=CharField(label=_('Description'),required=False,widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95'}))
    str_embed_code=CharField(label=_('Embed Code'),help_text="The Iframe code from vimeo or you tube",widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95'}))
    
    #str_url=URLField(label='URL',widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    #int_width=IntegerField(label='Width',widget=forms.TextInput(attrs={'size':'40','class':''}),required=False)
    #int_height=IntegerField(label='Height',widget=forms.TextInput(attrs={'size':'40','class':''}),required=False)
    #images=ModelMultipleChoiceField(queryset=Medias.objects.filter(str_type="photo"))
    class Meta:
        model=Medias
        fields = ('str_embed_code','str_name', 'str_description')#,'str_url') #,'int_width','int_height')
 


class ImageForm(ModelForm):

#    help_text="Use puns liberally",
    str_name=CharField(label=_('Title'),widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_description=CharField(label=_('Description'),required=False,widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95'}))
    str_file=FileField(label=_('File'))
    
    #str_url=URLField(label='URL',widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    int_width=IntegerField(label=_('Width'),widget=forms.TextInput(attrs={'size':'40','class':''}),required=False)
    int_height=IntegerField(label=_('Height'),widget=forms.TextInput(attrs={'size':'40','class':''}),required=False)
    #images=ModelMultipleChoiceField(queryset=Medias.objects.filter(str_type="photo"))
    class Meta:
        model=Medias
        fields = ('str_file','str_name', 'str_description')#,'str_url') #,'int_width','int_height')
    
class MediasForm(ModelForm):

    str_type=ChoiceField(choices=Medias.CONTENT_TYPE,required=True)
    str_name=CharField(label=_('Title'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_description=CharField(label=_('Description'),required=False,widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95'}))
    str_file=FileField(label=_('File'),required=False)
    str_url=CharField(label=_('URL'),widget=forms.TextInput(attrs={'size':'40','class':'text95'}),required=False)
    str_embed_code=CharField(label=_('Embed Code'),required=False,help_text=_("The Iframe code from vimeo or you tube"),widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95'}))
 
    #int_width=IntegerField(label='Width',widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    #int_height=IntegerField(label='Height',widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    #images=ModelMultipleChoiceField(queryset=Medias.objects.filter(str_type="photo"))
    class Meta:
        model=Medias
        fields = ('str_type','str_name', 'str_description','str_file','str_embed_code','str_url') #,'int_width','int_height')
        
class AlbumForm(ModelForm):
    str_type=ChoiceField(label=_('Type'),choices=MediaAlbum.ALBUM_TYPE)
    str_name=CharField(label=_('Title'),widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_description=CharField(label=_('Summary'),widget=forms.Textarea(attrs={'cols':'70','rows':'4','class':'text95'}))
    class Meta:
        model=Medias
        fields = ('str_type','str_name', 'str_description') #,'int_width','int_height')

class AddPhotoForm(forms.Form):
    images=ModelChoiceField(label=_('Image'),queryset=Medias.objects.filter(str_type="image"))
    int_width=IntegerField(label=_('Width'),widget=forms.TextInput(attrs={'size':'40','class':'text'}))
    int_height=IntegerField(label=_('Height'),widget=forms.TextInput(attrs={'size':'40','class':'text'}))
    
