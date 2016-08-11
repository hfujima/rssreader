# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta
from bs4 import BeautifulSoup
from bs4.element import Tag

from hfujima.rss.data import Rss, RssChannel, RssItem
from hfujima.rss.parser.base import RssParser


class BsRssParser(RssParser):
    __metaclass__ = ABCMeta

    def parse(self, data):
        soup = BeautifulSoup(data)
        rss = self._parse_soup(soup)

        return rss

    @abstractmethod
    def _parse_soup(self, soup):
        raise NotImplementedError()


class BsRssParserRss20(BsRssParser):
    def _parse_soup(self, soup):
        rss = Rss()

        rss_soup = self._parse_rss(soup)
        channel_soup = self._parse_channel(rss_soup)
        item_soups = self._parse_items(channel_soup)

        rss.channel = self._create_rss_channel(channel_soup)
        for item_soup in item_soups:
            i = self._create_rss_item(item_soup)
            rss.items.append(i)

        return rss

    @classmethod
    def _parse_rss(cls, soup):
        rss_list = soup.find_all(u'rss')
        if not rss_list:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'rss not find!')
        elif len(rss_list) >= 2:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'duplicate rss!')

        return rss_list[0]

    @classmethod
    def _parse_channel(cls, soup):
        channels = soup.find_all(u'channel')

        if not channels:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'channel not find!')
        elif len(channels) >= 2:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'duplicate channels!')

        return channels[0]

    @classmethod
    def _parse_items(cls, soup):
        return soup.find_all(u'item')

    @classmethod
    def _create_rss_channel(cls, soup):
        rss_channel = RssChannel()
        for c in soup.children:
            if isinstance(c, Tag) and c.name and hasattr(rss_channel, c.name):
                setattr(rss_channel, c.name, c.string)

        return rss_channel

    @classmethod
    def _create_rss_item(cls, soup):
        rss_item = RssItem()
        for c in soup.children:
            if isinstance(c, Tag) and c.name and hasattr(rss_item, c.name):
                setattr(rss_item, c.name, c.string)

        return rss_item
