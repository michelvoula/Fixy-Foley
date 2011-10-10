from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext as _
# Create your models here.

## Generic Media Class
class Medias(models.Model):
        CONTENT_TYPE = (
        (u'image', u'Image File'),
        (u'image_url', u'Image URL'),
        (u'video', u'Video'),        
        (u'video_url', u'Video URL'),
    )
        str_type=models.CharField(_("Type"),max_length=25, choices=CONTENT_TYPE,null=True,blank=True)
        str_name=models.CharField(_('Name'),max_length=50,null=True,blank=True)
        str_file=models.FileField(_('File'),upload_to='photos',null=True,blank=True)
        str_url=models.CharField(_('URL'),max_length=200,null=True,blank=True)
        str_description=models.CharField(_('Description'),max_length=50)
        str_embed_code=models.TextField(_('Embed Code'),blank=True,null=True)
        dt_add_date=models.DateTimeField(_("Creation Date"),default=datetime.now(),null=True,blank=True) #date of creation of post
        #int_width=models.IntegerField('Width',null=True,blank=True,default=0)
        #int_height=models.IntegerField('Height',null=True,blank=True,default=0)
        author= models.ForeignKey(User,blank=True,null=True)        
        def __unicode__(self):
            return self.str_name
        class Meta:
            verbose_name = _("File")
            verbose_name_plural = _("Files")
            
            
class MediaAlbum(models.Model):
        ALBUM_TYPE = (
        (u'image', u'Image'),
        (u'video', u'Video'),        
    )
        str_type=models.CharField(_("Type"),max_length=25, choices=ALBUM_TYPE)
        str_name=models.CharField(_('Name'),max_length=50)
        str_description=models.CharField(_('Description'),max_length=50)
        medias=models.ManyToManyField(_("Medias"),through='AlbumMedias')
        author= models.ForeignKey(User,blank=True,null=True)
        def __unicode__(self):
            return self.str_name
        class Meta:
            verbose_name = _("Video and Photo Gallery")
            verbose_name_plural = _("Videos and Photos Galleries")        
class AlbumMedias(models.Model):
    album= models.ForeignKey(MediaAlbum)
    media= models.ForeignKey(Medias)
    position=models.IntegerField(_("Position"),blank=False,default=0)
    