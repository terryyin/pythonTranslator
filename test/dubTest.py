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
from dub import dub_format_exception
from .utility import typeOFTranslatedLineInList

CODE_SYNTAXERROR = "1+\n"
CODE_NAMEERROR = 'not_defined\n'

class DubTest(unittest.TestCase):
    def generatorTraceback(self, code):
        import sys
        try:
            eval(code)
        except:
            etype, value, tb = sys.exc_info()
        traceList = dub_format_exception(etype, value, tb)
        return traceList

    def testSyntaxError(self):
        traceList = self.generatorTraceback(CODE_SYNTAXERROR)
        self.assertTrue(typeOFTranslatedLineInList('SyntaxError', traceList))

    def testNameError(self):
        traceList = self.generatorTraceback(CODE_NAMEERROR)
        self.assertTrue(typeOFTranslatedLineInList('NameError', traceList))
        self.assertFalse(typeOFTranslatedLineInList('SyntaxError', traceList))


if __name__ == "__main__":
    unittest.main()