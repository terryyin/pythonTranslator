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

from subprocess import Popen, PIPE
import os
import dub.resource as resource
from .utility import typeOFTranslatedLineInList
import sys

decode = [lambda x:x, lambda x:x.decode('UTF-8')][sys.version_info.major>2] 

class testDubForPythonInInteractiveMode(unittest.TestCase):
    def setUp(self):
        env = os.environ.copy()
        env["PYTHONSTARTUP"] = "dubShell.py"
        self.shell = Popen("python -i".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE, env = env)
        
    def testShouldSeeWelcomeInformation(self):
        stdout, stderr = self.shell.communicate("")
        self.assertIn(resource.WELCOME + resource.VERSION, decode(stderr))
        self.assertEqual('', decode(stdout))
        
    def testShouldSeeTranslatedSyntaxError(self):
        stdout, stderr = self.shell.communicate("1+\n".encode("UTF-8"))
        self.assertTrue(typeOFTranslatedLineInList('SyntaxError', decode(stderr).splitlines()))
        self.assertEqual('', decode(stdout))
        
    def testShouldNotSeeTranslatedSyntaxErrorWhenNoInput(self):
        stdout, stderr = self.shell.communicate("")
        self.assertFalse(typeOFTranslatedLineInList('SyntaxError', decode(stderr).splitlines()))
        self.assertEqual('', decode(stdout))

class testDubForPythonInProgramMode(unittest.TestCase):
    def testShouldSeeNoErrorWhenEverythingIsOK(self):
        self.shell = Popen("python test/example.py".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE)
        stdout, stderr = self.shell.communicate("")
        self.assertEqual([], decode(stderr).splitlines())
        
    def testShouldSeeTranslationOfTheError(self):
        self.shell = Popen("python test/example.py 1+\n".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE)
        stdout, stderr = self.shell.communicate("")
        self.assertTrue(typeOFTranslatedLineInList('SyntaxError', decode(stderr).splitlines()))

class testDubForProgramUsingTraceback(unittest.TestCase):
    def testShouldGetDualLanguageTraceback(self):
        import dub
        import traceback
        import sys
        try:
            eval("1+\n")
        except:
            etype, value, tb = sys.exc_info()
        traceList = traceback.format_exception(etype, value, tb)
        self.assertTrue(typeOFTranslatedLineInList('SyntaxError', traceList))
        
        
if __name__ == '__main__':
    unittest.main()