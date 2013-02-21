from django.db import models
import datetime
from django.utils import timezone
import logging
import re


logger = logging.getLogger('django.request')
pattern=re.compile('/\d{1,4}x\d{1,4}/')
IMAGE_WIDTH=200
IMAGE_HEIGHT=240

class Album(models.Model):
    name = models.CharField(max_length=200,unique=True)
    desc=models.CharField(max_length=500)
    url=models.CharField(max_length=500)
    rss=models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True,auto_now_add=True)
    
class Document(models.Model):
    name = models.CharField(max_length=200)
    url=models.CharField(max_length=500)
    digest=models.CharField(max_length=1024)
    pub_date= models.DateField('date published')
    num_photo=models.IntegerField(default=0)
    photo1=models.CharField(max_length=500,null=True)
    photo2=models.CharField(max_length=500,null=True)
    photo3=models.CharField(max_length=500,null=True)
    album=models.ForeignKey(Album)
    
    def dig(self):
        return 'dig'
    
    def setImages(self,images):
        count=0
        for img in images:
            count+=1
            if count==1:
                self.photo1=getImageSizeURL(img, IMAGE_WIDTH, IMAGE_HEIGHT)
            elif count==2:
                self.photo2=getImageSizeURL(img, IMAGE_WIDTH, IMAGE_HEIGHT)
            elif count==3:
                self.photo3=getImageSizeURL(img, IMAGE_WIDTH, IMAGE_HEIGHT)
                break
            else:
                pass #never go heppen!
        self.num_photo=count
    
def getImageSizeURL(image,width,height):
        sizeStr='/'+str(width)+'x'+str(height)+'/'
        result=re.sub(pattern,sizeStr,image)
        return result
        