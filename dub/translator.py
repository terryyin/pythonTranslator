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

import resource
import re

__errorTypePatterns = None

def _initPatterns():
    global __errorTypePatterns
    if __errorTypePatterns is None:
        regstr = '|'.join(["(?P<{0}>{0})".format(et) for et in resource.ExceptionTypes.keys()])
        __errorTypePatterns = re.compile(regstr)
    return __errorTypePatterns

def _translateLine(line):
    global __errorTypePatterns
    yield line
    m = __errorTypePatterns.match(line)
    if m:
        newLine = resource.ExceptionTypes[m.lastgroup]['name'] + ':'
        for detail in resource.ExceptionTypes[m.lastgroup]['detail']:
            dm = re.match(cFormatterToRegex(detail[0]), line[m.end() + 1:].lstrip())
            if dm:
                newLine += dm.expand(detail[1])
                break
        yield newLine + '\n'

def translateTraceList(traceList):
    _initPatterns()
    translatedList =[]
    for line in traceList:
        translatedList.extend(_translateLine(line))
    return translatedList

cFormatterPattern = re.compile("%\.?\d*s")
def cFormatterToRegex(cFormatterString):
    regex = cFormatterString
    m = cFormatterPattern.search(cFormatterString)
    if m:
        regex = regex.replace(m.group(0), "(.*)")
    return regex