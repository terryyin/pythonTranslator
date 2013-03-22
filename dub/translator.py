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

def translateTraceList(traceList):
    _initPatterns()
    translatedList =[]
    for line in traceList:
        translatedList.extend(_translateLine(line))
    return translatedList

__errorTypePatterns = None

def _initPatterns():
    global __errorTypePatterns
    if __errorTypePatterns is None:
        regstr = '|'.join(["(?P<{0}>{0})".format(et) for et in resource.ExceptionTypes.keys()])
        __errorTypePatterns = re.compile(regstr)
    return __errorTypePatterns

def _translateMessage(errorType, message):
    for msgPattern in resource.ExceptionTypes[errorType]['messages']:
        dm = re.match(cFormatterToRegex(msgPattern[0]), message.lstrip())
        if dm:
            return dm.expand(msgPattern[1])
    return message

def _translateLineOfType(errorType, message):
    return resource.ExceptionTypes[errorType]['name'] + ':' + _translateMessage(errorType, message) + "\n"

def _translateLine(line):
    global __errorTypePatterns
    yield line
    m = __errorTypePatterns.match(line)
    if m:
        yield _translateLineOfType(m.lastgroup, line[m.end() + 1:])

cFormatterPattern = re.compile(r"\\%\\?\.?\d*[sdR]")

def cFormatterToRegex(cFormatterString):
    regex = re.escape(cFormatterString)
    for m in cFormatterPattern.findall(regex):
        regex = regex.replace(m, "(.*)")
    return regex
