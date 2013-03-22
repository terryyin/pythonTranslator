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

WELCOME = "已启动Python中英文双语插件DUB"
VERSION = "0.1"
GITHUB = "https://github.com/terryyin/pythonTranslator"
ExceptionTypes = {
                  'SyntaxError':{
                                 'name':'语法错误',
                                 'detail':[("",'无效的语法')]},
                  'NameError':{
                               'name':'名字错误',
                               'detail':[("name '%.200s' is not defined",r"名字'\1'还没有定义")]},
                  'Traceback':{
                               'name' :'回溯追踪（最近的调用在最后）',
                               'detail':[('','')]},
                  }