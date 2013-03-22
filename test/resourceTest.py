#!/usr/bin/env python
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  author: terry.yinzhe@gmail.com
#

import unittest

from dub.translator import cFormatterToRegex

class TestCFormatterToRegex(unittest.TestCase):

    def testNoFormatter(self):
        self.assertEqual(r"regular\ String", cFormatterToRegex("regular String"))

    def testStringFormatter(self):
        self.assertEqual(r"name\ \'(.*)\'", cFormatterToRegex("name '%.200s'"))

    def testStringFormatterWithParen(self):
        self.assertEqual(r"\(\)", cFormatterToRegex("()"))

    def testStringFormatterMulitplePlaces(self):
        self.assertEqual("(.*)(.*)(.*)", cFormatterToRegex("%.100s%.200s%s"))


