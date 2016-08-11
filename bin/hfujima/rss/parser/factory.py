# -*- coding: utf-8 -*-
from hfujima.rss.parser.bs import BsRssParserRss20
from hfujima.rss.parser.sax import SaxRssParserRss20


class RssParserFactory(object):
    @classmethod
    def create(cls, xml_parser=u'sax', rss_version=u'rss2.0'):
        if xml_parser == u'sax':
            return cls.create_sax_parser(rss_version=rss_version)
        elif xml_parser == u'bs4':
            return cls.create_bs4_parser(rss_version=rss_version)
        else:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'unrecognized xml parser!')

    @classmethod
    def create_sax_parser(self, rss_version=u'rss2.0'):
        if rss_version == u'rss2.0':
            return SaxRssParserRss20()
        else:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'unsupported rss version!')

    @classmethod
    def create_bs4_parser(self, rss_version=u'rss2.0'):
        if rss_version == u'rss2.0':
            return BsRssParserRss20()
        else:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'unsupported rss version!')
