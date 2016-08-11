# -*- coding: utf-8 -*-
import urllib2


class FileReader(object):
    def __init__(self, path):
        self.path = path

    def read(self):
        f = open(self.path, 'rb')
        with f:
            return f.read()


class URLReader(object):
    def __init__(self, url):
        self.url_ = url

    def read(self):
        res = urllib2.urlopen(self.url_)
        try:
            return res.read()
        finally:
            res.close()
