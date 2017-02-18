#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#

from __future__ import unicode_literals
from builtins import chr
import sys

def is_leading_surrogate(code_unit):
    return 0xD800 <= code_unit <= 0xDBFF

def is_trailing_surrogate(code_unit):
    return 0xDC00 <= code_unit <= 0xDFFF

def decode_surrogate_pair(leading, trailing):
    return ((leading - 0xD800) << 10) + (trailing - 0xDC00) + 0x10000

def _from_unicode(unistr):
    return (ord(c) for c in unistr)

def _from_utf16(unistr):
    assert sys.maxunicode == 0xFFFF
    leading_surrogate = -1
    for utf16 in unistr:
        code_unit = ord(utf16)
        if leading_surrogate == -1:
            if is_leading_surrogate(code_unit):
                leading_surrogate = code_unit
            else:
                yield code_unit
        else:
            if is_trailing_surrogate(code_unit):
                # Valid surrogate pair
                code_point = decode_surrogate_pair(leading_surrogate, code_unit)
                yield code_point
                leading_surrogate = -1
            else:
                # Leading surrogate without trailing surrogate
                yield leading_surrogate
                if is_leading_surrogate(code_unit):
                    leading_surrogate = code_unit
                else:
                    yield code_point
                    leading_surrogate = -1
    # Dangling surrogate at end of input
    if leading_surrogate != -1:
        yield leading_surrogate

def _to_utf16(code_points):
    for code_point in code_points:
        if code_point <= 0xFFFF:
            yield chr(code_point)
        else:
            base = code_point - 0x10000
            high_surrogate = (base >> 10) + 0xD800
            low_surrogate = (base & 0x3FF) + 0xDC00
            yield chr(high_surrogate)
            yield chr(low_surrogate)

def _to_chars(code_points):
    return (chr(cp) for cp in code_points)

if sys.maxunicode == 0xFFFF:
    from_unicode = _from_utf16
    to_chars = _to_utf16
else:
    assert sys.maxunicode == 0x10FFFF
    from_unicode = _from_unicode
    to_chars = _to_chars

def to_unicode(code_points):
    return u''.join(to_chars(code_points))
