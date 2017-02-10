Unicode Code Points for Python
==============================

Until Python 3.3, the Python runtime could be compiled in one of two Unicode modes:

1. ``sys.maxunicode == 0x10FFFF``

   In this mode, Python's Unicode strings support the full range of Unicode code points from U+0000 to U+10FFFF. One code point is represented by one string element::

      >>> import sys
      >>> hex(sys.maxunicode)
      '0x10ffff'
      >>> len(u'\U0001F40D')
      1
      >>> [c for c in u'\U0001F40D']
      [u'\U0001f40d']

   This is the default for Python 2.7 on Linux, as well as universally on Python 3.3 and later across all operating systems.

2. ``sys.maxunicode == 0xFFFF``

   In this mode, Python's Unicode strings only support the range of Unicode code points from U+0000 to U+FFFF. Any code points from U+10000 through U+10FFFF are represented using a pair of string elements in the UTF-16 encoding::

      >>> import sys
      >>> hex(sys.maxunicode)
      '0xffff'
      >>> len(u'\U0001F40D')
      2
      >>> [c for c in u'\U0001F40D']
      [u'\ud83d', u'\udc0d']

   This is the default for Python 2.7 on macOS and Windows.

This runtime difference makes writing Python modules to manipulate Unicode strings as series of codepoints quite inconvenient.

The codepoints module
=====================

This module solves the problem by exposing APIs to convert Unicode strings to and from lists of code points, regardless of the underlying setting for ``sys.maxunicode``::

    >>> hex(sys.maxunicode)
    '0xffff'
    >>> snake = tuple(codepoints.from_unicode(u'\U0001F40D'))
    >>> len(snake)
    1
    >>> snake[0]
    128013
    >> hex(snake[0])
    '0x1f40d'
    >>> codepoints.to_unicode(snake)
    u'\U0001f40d'
