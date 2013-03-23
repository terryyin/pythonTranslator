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
from dub.translator import PythonMessageTranslator
from .testData import assertTypeOFTranslatedLine

class TranslatorTest(unittest.TestCase):
    def testTranslateEmptyList(self):
        traceList = PythonMessageTranslator().translateTraceList([])
        self.assertEqual([], traceList)

    def testTranslateTraceBack(self):
        traceList = PythonMessageTranslator().translateTraceList(['Traceback (most recent call last):\n'])
        self.assertTrue(traceList[0].startswith('Traceback (most recent call last):'))
        assertTypeOFTranslatedLine(self, traceList[1], 'Traceback')

    def testTranslateErrorWithArgument(self):
        line = PythonMessageTranslator().translateTraceList(["NameError: name 'xxx' is not defined\n"])[1]
        assertTypeOFTranslatedLine(self, line, 'NameError')
        self.assertIn('xxx', line)

    def testTranslateErrorWithMultipleArgument(self):
        line = PythonMessageTranslator().translateTraceList(["TypeError: unsupported operand type(s) for /: 'str' and 'int'"])[1]
        assertTypeOFTranslatedLine(self, line, 'TypeError')
        self.assertIn('str', line)
        self.assertIn('int', line)
        self.assertIn('/', line)
        
    def testAssertionError(self):
        line = PythonMessageTranslator().translateTraceList([r"AssertionError: 'xxx' not found in '\xe5\x90\x8d\xe5\xad\x97\xe9\x94\x99\xe8\xaf\xaf:\n'"])[1]
        assertTypeOFTranslatedLine(self, line, 'AssertionError')

    def testTranslateErrorWithMessageThatDoesntMatchAnyDefinedPattern(self):
        line = PythonMessageTranslator().translateTraceList(["TypeError: NOT_DEFINED"])[1]
        assertTypeOFTranslatedLine(self, line, 'TypeError')
        self.assertIn('NOT_DEFINED', line)
