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

from .resource import loadExceptionTypesFromFile, cFormatterToRegex
import re

class PythonMessageTranslator:
    def __init__(self):
        self._initPatterns()

    def translateTraceList(self, traceList):
        translatedList = []
        for line in traceList:
            translatedList.extend(self._translateLine(line))
        return translatedList

    def _initPatterns(self):
        self._ExceptionTypes = loadExceptionTypesFromFile()
        regstr = '|'.join(["(?P<{0}>{0})".format(et) for et in self._ExceptionTypes.keys()])
        self._errorTypePatterns = re.compile(regstr)
    
    def _translateMessage(self, errorType, message):
        for msgPattern in self._ExceptionTypes[errorType]['messages']:
            dm = re.match(cFormatterToRegex(msgPattern[0]), message.lstrip())
            if dm:
                return dm.expand(msgPattern[1])
        return message
    
    def _translateLineOfType(self, errorType, message):
        return self._ExceptionTypes[errorType]['name'] + ':' + self._translateMessage(errorType, message) + "\n"
    
    def _translateLine(self, line):
        yield line
        m = self._errorTypePatterns.match(line)
        if m:
            yield self._translateLineOfType(m.lastgroup, line[m.end() + 1:])

    def getWelcome(self):
        return self._ExceptionTypes['welcome']
    
    def getTraceTitle(self):
        return ['Traceback (most recent call last):\n', self._ExceptionTypes['Traceback']['name']+'\n']
    