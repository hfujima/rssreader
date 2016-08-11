# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta


class RssParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, data):
        raise NotImplementedError()
