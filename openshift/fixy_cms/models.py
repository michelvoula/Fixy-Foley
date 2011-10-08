from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext as _
from django.conf import settings
import os


# Create your models here.

#if we want some special fields for a post we can specify them here    
post_template_dir=os.path.join(settings.TEMPLATE_DIR, 'post/display_templates')

class Category(models.Model):
    str_name=models.CharField(_('Name'),max_length=50)
    parent= models.ForeignKey(_("Category"),null=True,blank=True)
    def __unicode__(self):
        return self.str_name


class PostTemplate(models.Model):
    str_name=models.SlugField(_('Name'),max_length=50)
    str_file=models.FileField(_('File'),upload_to='templates',null=True,blank=True)
    def __unicode__(self):
        return self.str_name


    
class Post(models.Model):
    POST_STATUS = (
        (u'published', u'Approved'),
        (u'writing', u'Writing'),)
    str_post_title=models.CharField(_('Title'),max_length=50)
    str_post_type=models.CharField(_('Type'),max_length=50,blank=True,null=True)
    int_nb_comments=models.IntegerField(_('Number of Comments'),default=0)
    int_menu_order=models.IntegerField(_('Menu Order'),default=0)
    dt_post_date=models.DateTimeField(_("Creation Date"),default=datetime.now()) #date of creation of post
    dt_post_date_modified=models.DateTimeField(_("Last Modification Date"),default=datetime.now())
    str_post_summary=models.TextField(_('Summary')) #post or article summary
    str_slug=models.SlugField(_('Slug'),max_length=50,blank=False,null=False) #excerpt as in wordpress
    str_post_status=models.CharField(_('Status'),choices=POST_STATUS,max_length=50,blank=True,null=True) #what'sthe status
    str_comment_status=models.BooleanField(_('Comment Status'),blank=True) #are comment allowed?
    author= models.ForeignKey(User,blank=True,null=True)
    template= models.ForeignKey(PostTemplate,blank=True,null=True)
    #category=models.ManyToManyField(_("Category"),through='PostCategory')
    str_post_content=models.TextField(_('Content'),null=True,blank=True)

    def __unicode__(self):
        return self.str_post_title
    class Admin:
            js = ['tiny_mce/tiny_mce.js', 'js/textareas.js']



class PostCategory(models.Model):
    post= models.ForeignKey(Post)
    category= models.ForeignKey(Category)

class PostKeyWord(models.Model):
    str_name=models.CharField(_('Name'),max_length=50)
    post= models.ForeignKey(Post)

#Comments on a Post  

class Comments(models.Model):
    COMMENT_STATUS = (
        (u'approved', u'Approved'),
        (u'pending', u'Waiting Approbation'),
        (u'not_approved', u'Approved'),
    )
    str_name=models.TextField('Content')
    str_status = models.CharField(max_length=25, choices=COMMENT_STATUS)
    post= models.ForeignKey(Post)

class PostSpecialField(models.Model):
    str_field=models.CharField(_('Name'),max_length=50)
    str_value=models.CharField(_('Value'),max_length=50)
    post= models.ForeignKey(Post)
    

