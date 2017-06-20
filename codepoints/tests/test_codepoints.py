#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#

from nose_parameterized import parameterized
from nose.tools import assert_equal
import codepoints


@parameterized([
    (u'', ()),
    (u'abc', (97, 98, 99)),
    (u'\u1234\uABCD\uFEED', (0x1234, 0xABCD, 0xFEED)),
    (u'\U0001ABCD\U0002BCDE\U0003CDEF', (0x1ABCD, 0x2BCDE, 0x3CDEF)),
    (u'a\uD82A', (97, 55338)),
    (u'a\uD82Ac', (97, 55338, 99)),
    (u'a\uD82A\uD82A', (97, 55338, 55338)),
    (u'a\uD82A\uD82Ac', (97, 55338, 55338, 99)),
    (u'a\uDFCD', (97, 57293)),
    (u'a\uDFCDc', (97, 57293, 99)),
    (u'a\uDFCD\uDFCD', (97, 57293, 57293)),
    (u'a\uDFCD\uDFCDc', (97, 57293, 57293, 99)),
])
def test_to_and_from_unicode(unistr, code_points):
    assert_equal(code_points, tuple(codepoints.from_unicode(unistr)))
    assert_equal(unistr, codepoints.to_unicode(code_points))
