# -*- coding: utf-8 -*-
import pytz
import sys
from argparse import ArgumentParser, RawTextHelpFormatter

from hfujima.lib.functions import truncate
from hfujima.rss.parser.factory import RssParserFactory
from hfujima.rss.reader import FileReader, URLReader


class ResultWriter(object):
    def __init__(
            self, fmt,
            dt_format=u'%Y-%m-%d %H:%M:%S %z', time_zone=pytz.timezone('Asia/Tokyo'),
            out=sys.stdout, title_max_length=10, description_max_length=30):
        self.fmt = fmt
        self.dt_format = dt_format
        self.time_zone = time_zone
        self.out = out
        self.title_max_length = title_max_length
        self.description_max_length = description_max_length

    def write(self, rss):
        for item in rss.items:
            self.write_item(item)

    def write_item(self, item):
        self.out.write(
            self.fmt.format(
                title=truncate(item.title, self.title_max_length),
                description=truncate(item.description, self.description_max_length),
                pubDate=item.pubDate.astimezone(self.time_zone).strftime(self.dt_format),
            )
        )
        self.out.write(u'\n')


class Command(object):
    def execute(self):
        args = self._get_args()

        reader = FileReader if args.file else URLReader

        for url_or_path in args.url_or_path:
            # read
            data = reader(url_or_path).read()

            # parse
            parser = RssParserFactory.create()
            rss = parser.parse(data)

            # output
            ResultWriter(args.format).write(rss)

    @classmethod
    def _get_args(cls):
        parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

        parser.add_argument(
            u'url_or_path',
            type=unicode,
            nargs=u'+',
            help=u'rss feedのURLまたはRSSファイルのパス\n'
                 u'RSSファイルを指定する場合は--fileオプションを指定してください',
        )

        parser.add_argument(
            u'--file',
            action=u'store_true',
            help=u'RSSファイルを指定する場合にこのオプションを指定してください'
        )

        parser.add_argument(
            u'-f',
            u'--format',
            type=unicode,
            default=u'title:{title}, description:{description}, pubDate:{pubDate}',
            help=u'出力フォーマット\n'
                 u'default: "title:{title}, description:{description}, pubDate:{pubDate}"'
        )

        parser.add_argument(
            u'--rss-version',
            type=unicode,
            # 意外とバージョンがたくさんあるらしいけど今回はrss2.0だけ対応
            # choices=[u'rss0.9', ... , u'rss1.0', u'rss2.0', u'atom1.0', ...],
            choices=[u'rss2.0'],
            default=u'rss.2.0',
            help=u'RSSのバージョンが指定できます。'
        )

        return parser.parse_args()


if __name__ == u'__main__':
    Command().execute()
