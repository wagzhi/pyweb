# coding=gbk
from django.template import Context, loader
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from p_album.models import Album, Document
from p_album.sync import SyncAlbum
from django.core.context_processors import csrf
from django.template import RequestContext

def upload(request):
    files= request.FILES
    f=files['attch']
    fs=FileSystemStorage()
    fs.save(f.name,f)
    return HttpResponse('upload: '+f.name)


def detail(request,album_id):
    '''
        /{album_id}.html
    '''
    album=Album.objects.get(pk=album_id)
        
    syncAlbum=SyncAlbum(album)
    rssDom=syncAlbum.getRssDom(syncAlbum.getRssXml())
    docs=syncAlbum.getDocumentsFromRss(rssDom)
    pubDate=syncAlbum.getAlbumPubDate(rssDom)
        
    c=RequestContext(request,{
               'album':album,
               'date':pubDate.strftime('%Y-%m-%d %H:%M:%S'),
               'docs':docs
               })
    
    tt = loader.get_template('detail.html')
    return HttpResponse(tt.render(c))

def index(request):
    tt = loader.get_template('index.html')
    albums=Album.objects.all();
    c=RequestContext(request,{
               'albums':albums
               })
    return HttpResponse(tt.render(c))

def form(request):
    msg=''
     
    tt = loader.get_template('form.html')

    albums=Album.objects.all();
    album_names=''
    for album in albums:
        album_names+=','+album.name
    
    request.session['name']='paul wang'
    fs=FileSystemStorage()
    fs.save("hello.txt", ContentFile('new content'))
    
    c=Context({
               'path': os.path.dirname(__file__) ,
               'albums':album_names
               })
    c.update(csrf(request))
    return HttpResponse(tt.render(c))
    #t = loader.get_template('templates/index.html')
    #c = Context({
    #})
    #return HttpResponse(t.render(c))