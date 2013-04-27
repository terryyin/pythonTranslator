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

import sys
import traceback
from .translator import PythonMessageTranslator

__traceback_format_exception_only = traceback.format_exception_only
__traceback_format_exception = traceback.format_exception

def dub_format_exception_only(etype, value, limit=None):
    traceList = __traceback_format_exception_only(etype, value)
    return PythonMessageTranslator().translateTraceList(traceList)

def dub_format_exception(etype, value, tb, limit=None):
    if tb:
        list = PythonMessageTranslator().getTraceTitle()
        list = list + traceback.format_tb(tb, limit)
    else:
        list = []
    list = list + dub_format_exception_only(etype, value)
    return list

traceback.format_exception_only = dub_format_exception_only

def excepthook(exctype, value, tb):
    sys.stderr.writelines(dub_format_exception(exctype, value, tb))
    
sys.excepthook = excepthook

if __name__ == '__main__':
    pass
