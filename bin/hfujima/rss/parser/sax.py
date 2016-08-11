# -*- coding: utf-8 -*-
import xml.sax
from abc import abstractmethod, ABCMeta
from xml.sax.handler import ContentHandler

from hfujima.rss.data import Rss, RssChannel, RssItem
from hfujima.rss.parser.base import RssParser


class Rss20Handler(ContentHandler):
    def __init__(self):
        ContentHandler.__init__(self)
        self.rss = None

        self._start_handler_stack = []
        self._end_handler_stack = []
        self._target_stack = []
        self._current_node = u'root'
        self._char_chunks = []

    def startElement(self, name, attrs):
        self._current_node = name

        if self._start_handler_stack:
            self._start_handler_stack[-1](name, attrs)

        elif name == u'rss':
            if self.rss:
                # TODO: 適切なエラークラスを使う
                raise Exception(u'duplicate rss!')

            self.rss = Rss()
            version = attrs.get('version')
            if version != u'2.0':
                # TODO: 適切なエラークラスを使う
                raise Exception(u'unsupported version!')

        elif name == u'channel':
            self._start_channel_element(name, attrs)

    def endElement(self, name):
        self._set_value()

        if self._end_handler_stack:
            self._end_handler_stack[-1](name)

        self._current_node = u''
        self._char_chunks = []

    def endDocument(self):
        if not self.rss or not self.rss.channel:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'rss or channel not find!')

    def characters(self, char):
        char = char.strip()
        if char and self._current_node:
            self._char_chunks.append(char)

    def _set_value(self):
        if not self._target_stack:
            # データの格納先が存在しない
            return

        attr_name = self._current_node
        if attr_name.startswith('_'):
            # アンスコ始まりの属性は内部変数扱いで無視する
            return

        target = self._target_stack[-1]
        if hasattr(target, attr_name):
            setattr(target, attr_name, u''.join(self._char_chunks))

    def _start_channel_element(self, name, attrs):
        """"<channel>検出時の処理"""
        if not self.rss:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'rss not find!')

        if self.rss.channel:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'duplicate channel!')

        self.rss.channel = RssChannel()
        self._start_handler_stack.append(self._handle_channel_child)
        self._end_handler_stack.append(self._handle_channel_end)
        self._target_stack.append(self.rss.channel)

    def _handle_channel_child(self, name, attrs):
        """"<channel>の子ノードを処理"""
        if name == u'item':
            self._start_item_element(name, attrs)

    def _handle_channel_end(self, name):
        """"</channel>検出時の処理"""
        if name == u'channel':
            self._start_handler_stack.pop()
            self._end_handler_stack.pop()
            self._target_stack.pop()

    def _start_item_element(self, name, attrs):
        """"<item>検出時の処理"""
        if not self.rss:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'rss not find!')

        if not self.rss.channel:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'rss.channel not find!')

        item = RssItem()
        self.rss.items.append(item)

        if self.rss.channel:
            self.rss.channel = RssChannel()
            self._start_handler_stack.append(self._handle_item_child)
            self._end_handler_stack.append(self._handle_item_end)
            self._target_stack.append(item)
        else:
            # TODO: 適切なエラークラスを使う
            raise Exception(u'duplicate channel!')

    def _handle_item_child(self, name, attrs):
        """"<item>の子ノードを処理"""
        pass

    def _handle_item_end(self, name):
        """"</item>検出時の処理"""
        if name == u'item':
            self._start_handler_stack.pop()
            self._end_handler_stack.pop()
            self._target_stack.pop()


class SaxRssParser(RssParser):
    __metaclass__ = ABCMeta

    def parse(self, data):
        handler = self._create_handler()
        xml.sax.parseString(data, handler)

        return handler.rss

    @abstractmethod
    def _create_handler(self):
        raise NotImplementedError


class SaxRssParserRss20(SaxRssParser):
    def _create_handler(self):
        return Rss20Handler()
