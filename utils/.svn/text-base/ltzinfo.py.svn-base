# coding=gbk
import datetime
class Shanghai(datetime.tzinfo):
    def utcoffset(self,dt):
        return datetime.timedelta(hours=8)
    def tzname(self,dt):
        return 'Shanghai/Asia'
    def dst(self,dt):
        return datetime.timedelta(0)
    
class GMT(datetime.tzinfo):
    def utcoffset(self,dt):
        return datetime.timedelta(0)
    def tzname(self,dt):
        return 'GMT'
    def dst(self,dt):
        return datetime.timedelta(0)
    
gmt=GMT()
shanghai=Shanghai()