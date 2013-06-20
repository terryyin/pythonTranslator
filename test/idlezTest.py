#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from dub_src.ZShell import ZShell
from idlelib import PyShell

class TestIdleZ(unittest.TestCase):

    def testItWillModifyTheMenu(self):
        shell = ZShell()
        shell.hackPyShell(PyShell.PyShell)
        self.assertEquals(("file", "文件"), PyShell.PyShell.menu_specs[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()