# coding=gbk
'''
Created on 2012-11-3

@author: Paul <wagzhi@gmail.com>
'''
from p_album.models import Album, Document
import urllib
import xml.dom.minidom
import datetime
from django.utils import timezone
import HTMLParser
import logging
import re


logger = logging.getLogger('django.request')
pattern=re.compile('/\d{1,4}x\d{1,4}/')
IMAGE_WIDTH=200
IMAGE_HEIGTH=240

class SyncAlbum:
    '''doc'''
    GMT_TIME_FORMAT='%a, %d %b %Y %H:%M:%S GMT'
    
    def __init__(self,album):
        self.album=album
        
        
    def getRssXml(self):
        '''
                            获取制定album的rss内容
        '''
        rssUrl=self.album.rss
        rssfile=urllib.urlopen(rssUrl)
        return rssfile.read()
    
    def getRssDom(self,rssXml):
        rsc_utf8=rssXml.decode('gb2312').encode('utf-8').replace('gb2312','utf-8',1)
        return xml.dom.minidom.parseString(rsc_utf8)
    
    def getAlbumPubDate(self,rssDom):
        strAlbumPubDate=self.getValueNodeValue(rssDom, 'lastBuildDate')
        return self.parseGMTDate(strAlbumPubDate)
        
    def getDocumentsFromRss(self,rssdom):
        """
                         解析rss里的帖子内容，返回document对象列表
                         其中rss中的pubDate:
                         目前只支持'Tue, 06 Nov 2012 00:34:43 GMT'的日期格式，其它格式会抛异常。
                         时间为标准时间，程序转换为当前django时区（+8）
        """
        channel =rssdom.getElementsByTagName('channel')[0]
        items=channel.getElementsByTagName('item')
        docs=[]
        for item in items:
           d_name = self.getValueNodeValue(item, 'title')
           d_url=self.getValueNodeValue(item, 'link')
           d_digest=self.getValueNodeValue(item, 'description')
           s_pub_date=self.getValueNodeValue(item, 'pubDate')
           d_pub_date=self.parseGMTDate(s_pub_date)
           try:
               digests=self.parseDigest(d_digest)
               model=Document(name=d_name,url=d_url,digest=digests[0],pub_date=d_pub_date)
               model.setImages(digests[1])
              
               model.album=self.album
               docs.append(model)
           except UnicodeEncodeError,e:
               logger.error(u'encode err when parse digest of document '+d_name)              
           
        return docs
    
    def parseGMTDate(self,dateString):
         '''
         parse date string like 'Tue, 06 Nov 2012 00:34:43 GMT' and convert timezone from gmt to current time zone(set in settings.py).
         '''
         d_pub_date=datetime.datetime.strptime(dateString,self.GMT_TIME_FORMAT) 
         d_pub_date=d_pub_date.replace(tzinfo=timezone.utc).astimezone(timezone.get_current_timezone())
         return d_pub_date
     
    def parseDigest(self,degest):
        parser=DocumentDigParser()
        parser.feed(degest)
        
        gbk=parser.pureText.encode('gbk')
        return (parser.pureText,parser.images)
        
    def getValueNodeValue(self ,item,tagName):
        '''
         item : parent node
         tagName : child node of the item, contains text data
         return a string contains all text
        '''
        nameNode=item.getElementsByTagName(tagName)[0]
        nodelist=nameNode.childNodes
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)
    
    def getImageSizeURL(self,image,width,height):
        sizeStr='/'+str(width)+'x'+str(height)+'/'
        result=re.sub(pattern,sizeStr,image)
        return result
    
class DocumentDigParser(HTMLParser.HTMLParser):
    pureText=''
    images=[]
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.images=[] #如果不重新复制，这个images对象不会重新构建，一直增加。
        
    def handle_starttag(self, tag, attrs):
        if tag=='IMG' or tag=='img':
            for name, value in attrs:
                self.images.append(value)
    def handle_data(self, data):
        self.pureText+=data