# -*- coding: utf-8 -*-
from datetime import datetime
from email.utils import mktime_tz, parsedate_tz

import pytz


class Rss(object):
    def __init__(self):
        self.channel = None
        self.items = []


class RssChannel(object):
    def __init__(self):
        self.title = None
        self.link = None
        self.description = None
        self.language = None
        self.copyright = None
        self.managingEditor = None
        self.webMaster = None
        self._pubDate = None
        self.lastBuildDate = None
        self.category = None
        self.generator = None
        self.docs = None
        self.cloud = None
        self.ttl = None
        self.image = None
        self.rating = None
        self.textInput = None
        self.skipHours = None
        self.skipDays = None

    @property
    def pubDate(self):
        return None

    @pubDate.setter
    def pubDate(self, str_value):
        if not str_value:
            self._pubDate = None

        t = parsedate_tz(str_value)
        if t is None:
            self._pubDate = None

        timestamp = mktime_tz(t)
        self._pubDate = datetime.fromtimestamp(timestamp, pytz.utc)

    @pubDate.getter
    def pubDate(self):
        return self._pubDate


class RssItem(object):
    def __init__(self):
        self.title = None
        self.link = None
        self.description = None
        self.author = None
        self.category = None
        self.comments = None
        self.enclosure = None
        self.guid = None
        self._pubDate = None
        self.source = None

    @property
    def pubDate(self):
        return None

    @pubDate.setter
    def pubDate(self, str_value):
        if not str_value:
            self._pubDate = None

        t = parsedate_tz(str_value)
        if t is None:
            self._pubDate = None

        timestamp = mktime_tz(t)
        self._pubDate = datetime.fromtimestamp(timestamp, pytz.utc)

    @pubDate.getter
    def pubDate(self):
        return self._pubDate
