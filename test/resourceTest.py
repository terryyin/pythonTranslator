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
from dub.resource import LoadExceptionTypesInfo
from dub.resource import DUBLoadError

class TestCFormatterToRegex(unittest.TestCase):

    def testNoFormatter(self):
        self.assertEqual(r"regular\ String", cFormatterToRegex("regular String"))

    def testStringFormatter(self):
        self.assertEqual(r"name\ \'(.*)\'", cFormatterToRegex("name '%.200s'"))

    def testStringFormatterForDigits(self):
        self.assertEqual(r"(.*)", cFormatterToRegex("%d"))

    def testStringFormatterForObjects(self):
        self.assertEqual(r"(.*)", cFormatterToRegex("%R"))

    def testStringFormatterWithParen(self):
        self.assertEqual(r"\(\)", cFormatterToRegex("()"))

    def testStringFormatterMulitplePlaces(self):
        self.assertEqual("(.*)(.*)(.*)", cFormatterToRegex("%.100s%.200s%s"))


START_TOKEN = "DUB Python Error Message Translator\n=====\n"
class TestLoadResourceFile(unittest.TestCase):
    
    def test_ShouldRaiseWhenNoStartTokenFound(self):
        self.assertRaisesRegexp(DUBLoadError, "No expection info found", lambda:LoadExceptionTypesInfo("DUB Python Error Message Translator\n++++\n"))

    def test_ShouldRaiseWhenStartTokenNotEndedWithSeparators(self):
        self.assertRaisesRegexp(DUBLoadError, "No expection info found", lambda:LoadExceptionTypesInfo("balh\nblah"))

    def test_ShouldReturnEmptyTypesWhenStartTokenFound(self):
        types = LoadExceptionTypesInfo(START_TOKEN)
        self.assertEqual(0, len(types))
    
    def test_ShouldReturnTypeWhenDefined(self):
        types = LoadExceptionTypesInfo(START_TOKEN + 
                    "##SomeError: SomeErrorInOtherLanguage\n" 
                )
        self.assertEqual(1, len(types))
        self.assertIn("SomeError", types)
        self.assertEqual("SomeErrorInOtherLanguage", types["SomeError"]['name'])
        
    def test_ShouldReturnTypeWithMessageWhenDefined(self):
        types = LoadExceptionTypesInfo(START_TOKEN + 
                    "##SomeError: SomeErrorInOtherLanguage\n" +
                    "###message1\n" +
                    "translation1\n" +
                    "###message2\n" +
                    "translation2\n" +
                    "##OtherError:\n"
                )
        self.assertEqual(["message1","translation1"], types["SomeError"]['messages'][0])
        self.assertEqual(["message2","translation2"], types["SomeError"]['messages'][1])
        


