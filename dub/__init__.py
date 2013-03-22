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
from translator import translateTraceList

__traceback_format_exception = traceback.format_exception

def dub_format_exception(etype, value, tb, limit=None):
    traceList = __traceback_format_exception(etype, value, tb, limit)
    return translateTraceList(traceList)

traceback.format_exception = dub_format_exception

def excepthook(exctype, value, tb):
    sys.stderr.writelines(dub_format_exception(exctype, value, tb))
    
sys.excepthook = excepthook

if __name__ == '__main__':
    pass
