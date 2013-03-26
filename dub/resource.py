#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Licensed under the Apache License, Version 2.0 [(the "License")];
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

import re, os, sys

VERSION = "0.1"
GITHUB = "https://github.com/terryyin/pythonTranslator"
ENCODE = "utf-8"
RESOURCE_FOLDER = "dub_resource"

openReadOnly = [lambda f:open(f, 'r'), lambda f:open(f, 'r', encoding=ENCODE)][sys.version_info.major >2]

def loadExceptionTypesFromFile(resourceFile="README.md"):
    global ExceptionTypes
    if not os.path.exists(resourceFile):
        resourceFile = sys.prefix + "/" + RESOURCE_FOLDER + "/" + resourceFile
    with openReadOnly(resourceFile) as f:
        return LoadExceptionTypesInfo(f.read())
    

class DUBLoadError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

def LoadExceptionTypesInfo(doc):
    start = doc.find("WELCOME\n=")
    if start >=0:
        types = {}
        lines = doc[start:].splitlines()[2:]
        if len(lines) > 0 and not lines[0].startswith("##"):
            types['welcome'] = lines[0]
            lines = lines[1:]
        currentMessages = []
        for line in doc[start:].splitlines()[2:]:
            line = line.strip()
            if len(line) > 0:
                if line.startswith("###"):
                    currentMessages.append([line[3:],""])
                elif line.startswith("##"):
                    errorName = line[2:].split(':', 1)
                    currentMessages = []
                    types[errorName[0].strip()] = {'name':errorName[1].strip(), 'messages' : currentMessages}
                else:
                    if len(currentMessages) > 0:
                        currentMessages[-1][1] = line
        return types
    error = DUBLoadError("No expection info found")
    raise error

cFormatterPattern = re.compile(r"\\%\\?\.?\d*[sdR]")

def cFormatterToRegex(cFormatterString):
    regex = re.escape(cFormatterString)
    for m in cFormatterPattern.findall(regex):
        regex = regex.replace(m, "(.*)")
    return regex
