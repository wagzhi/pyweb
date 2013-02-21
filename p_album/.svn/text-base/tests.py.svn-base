# coding=gbk
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import timezone, dateparse

from django.test import TestCase
import datetime
import urllib
import os
import xml.dom.minidom
from p_album.models import Album, Document
from p_album.sync import SyncAlbum
from utils import ltzinfo

rs='''<?xml version="1.0" encoding="gbk"?>
<rss>
  <channel>
    <title>美女模特</title>
    <link>http://www.19lou.com/r/mvmt.html</link>
    <description>333</description>
    <language>zh-cn</language>
    <copyright>3</copyright>
    <lastBuildDate>Tue, 06 Nov 2012 09:41:52 GMT</lastBuildDate>
    <generator>www.19lou.com</generator>
    <ttl>10</ttl>
  </channel>
</rss>
'''

class SimpleTest(TestCase):    
    fixtures = ['p_album/initial_data.json']
    def setUp(self):
        print('this is setup...')
        
    def testCreateAlbum(self):
        Album.objects.create(name=u'19楼早知道',desc=u'19楼早知道花坛',url='http://www.19lou.com/r/mvmt.html',rss='http://www.19lou.com/r/rss/682585627.html',pub_date=datetime.datetime.now())
        albums=Album.objects.all()
        count=Album.objects.count()
        self.assertEqual(count, 3, "album number should be 3 but "+str(count)+".")
        
    def testGetDocumentsFromRss(self):
        rssFile = open(os.path.dirname(__file__)+'/sample_rss.xml')
        rssStr=rssFile.read()
        syncAlbum=SyncAlbum(Album.objects.all()[0])
        rssDom=syncAlbum.getRssDom(rssStr)
        albumPubdate=syncAlbum.getAlbumPubDate(rssDom)
        self.assertEqual(albumPubdate.hour, 15, "GMT 7,should be 15 in +8")
        
        docs=syncAlbum.getDocumentsFromRss(rssDom)
        self.assertEqual(len(docs), 30, 'There shold be 30 document in the sample but '+str(len(docs)))
        doc=docs[0]
        self.assertEqual(doc.name, u'【张力视觉】杭州大厦最美瞬间之模特琪琪', doc.name+' is not correct value in sample file:sample_rss.xml')
        self.assertEqual(doc.pub_date.hour,8,u'The rigth time should be 8 but '+ str(doc.pub_date.hour))
        #test this doc can be saved
        doc.save()
        self.assertEqual(Document.objects.count(),1,'document number should be 1 but '+str(Document.objects.count()))
        self.assertEqual(doc.pk,1,'id shold be 1 but '+ str(doc.pk))
        self.assertEqual(doc.num_photo,3,'photo num should be 3 int thi doc.')
        self.assertEqual(doc.digest,u'周六参加了杭州大厦最美瞬间摄影比赛，各种大师 ，各种美女帅哥，尤其是模特琪琪，表现力十足，这里先上一组琪琪的照片，要约拍的点这里...','pure text no macth')
        print doc.photo1
        print doc.photo2
    
    def testGetImageSizeURL(self):
        img='http://att3.citysbs.com/120x120/hangzhou/2012/11/18/18/181218_14231353233538445_caed40dbbdc1e81fc0f107040e024402.jpg'
        img2='http://att3.citysbs.com/200x240/hangzhou/2012/11/18/18/181218_14231353233538445_caed40dbbdc1e81fc0f107040e024402.jpg'
        syncAlbum=SyncAlbum(Album.objects.all()[0])
        newImg=syncAlbum.setImageSize(img, 200, 240)
        self.assertEquals(newImg,img2,'should be eqauls')
        
    def __test_basic_addition(self):
        """
        some demo code but not testcase now!
        
        TODO: how to create another tests file in this app(p_album)?
        """
        album= Album.objects.all()[0]
        rssfile=urllib.urlopen(album.rss)
        rsc=rssfile.read()
        rsc_utf8=rsc.decode('gb2312').encode('utf-8').replace('gb2312','utf-8',1)
        rssdom = xml.dom.minidom.parseString(rsc_utf8)
        channel =rssdom.getElementsByTagName('channel')
        for c in channel:
            title=c.getElementsByTagName('title')[0]
            #str= getText(title.childNodes)
            #print str.__class__
            
        self.assertEqual(1 + 1, 2)
