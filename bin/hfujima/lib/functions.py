# -*- coding: utf-8 -*-


def truncate(text, max_length, suffix=u'…', return_none=False):
    """
    一定文字数を超えた文字列を「…」などで置換する。
    suffixがmax_lengthより長い場合、suffixをmax_lengthまで切り詰めた文字を返却する。
    :param text: 整形対象のテキスト
    :param max_length: 表示する文字数(suffix込)
    :param suffix: max_lengthを超えた文字列を置換する文字列
    :param return_none: Trueの場合はtextがNoneだった場合にNoneを返却する。Falseの場合は空文字列を返却する
    :return: unicode
    >>> print truncate(u'aaaaa', 3)
    aa…
    >>> print truncate(u'漢字です', 1)
    …
    >>> print truncate(u'漢字', 2)
    漢字
    >>> print truncate(u'漢字です', 2)
    漢…
    >>> print truncate(u'あいうえお', 5, u'・・・')
    あいうえお
    >>> print truncate(u'あいうえお', 4, u'・・・')
    あ・・・
    """
    if text is None:
        if return_none:
            return None
        else:
            return u''

    if max_length < len(text):
        return text[:max_length - len(suffix)] + suffix
    return text
