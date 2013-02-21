'''
Created on 2012-11-6

@author: DELL
'''
from django.test import TestCase

class SyncTests(TestCase):
    def setUp(self):
        print 'this is syncTest!'
    def test_GetDocumentsFromRss(self):
        self.assertEqual(1 + 1, 2)
