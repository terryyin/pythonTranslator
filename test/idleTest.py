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
from idlelib.PyShell import ModifiedInterpreter
from .testData import typeOFTranslatedLineInList

class FakeText:
    def tag_add(self, *arg):pass
    def see(self, *arg):pass
    def get(self, *arg):pass
    def tag_remove(self, *arg):pass
    
class FakeTkConsole:
    def __init__(self):self.text = FakeText()
    def resetoutput(self):pass
    def getvar(self, *var):return False
    def showprompt(self, *arg):pass
    def colorize_syntax_error(self, *arg):pass
    
class MyInteractiveInterpreter(ModifiedInterpreter):
    def __init__(self):
        ModifiedInterpreter.__init__(self, FakeTkConsole())
        self.output = ""
        
    def write(self, cont):
        self.output += cont
    
class TestIDLE(unittest.TestCase):
    def setUp(self):
        self.output = ""
        
    def test_ShouldWorkWithIDLE(self):
        import dub
        ii = MyInteractiveInterpreter()
        try:
            {}+1
        except:
            ii.showtraceback()
        print ("$$$$$$$$$$$$$$$$$$$$$$$$$$\n"+ii.output)
        self.assertTrue(typeOFTranslatedLineInList('TypeError', ii.output.splitlines()))

    def test_SyntaxErrorShouldWorkWithIDLE(self):
        import dub
        ii = MyInteractiveInterpreter()
        #ModifiedInterpreter.showsyntaxerror = lambda filename: None
        try:
            eval('"')
        except:
            ii.showsyntaxerror()
        self.assertIn("SyntaxError", ii.output)
        self.assertTrue(typeOFTranslatedLineInList('SyntaxError', ii.output.splitlines()))
