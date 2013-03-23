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

import re

def assertTypeOFTranslatedLine(self, line, errorType):
    global ExceptionTypes
    return self.assertTrue(line.startswith(ExceptionTypes[errorType]['name']))

def typeOFTranslatedLineInList(errorType, traceList):
    global ExceptionTypes
    p = re.compile(re.escape(ExceptionTypes[errorType]['name']))
    for line in traceList:
        if p.match(line):
            return True
    return False

WELCOME = "已启动Python中英文双语插件DUB"

ExceptionTypes = {
                  'SyntaxError':{
                                 'name':'语法错误',
                                 'messages':[("invalid syntax",r"无效的语法"),
                                        ("invalid token",r'无效的单词'),
                                        ("EOF while scanning triple-quoted string literal",r"扫读三个引号括起的字符串文本时遇到了EOF文件结尾"),
                                        ("EOL while scanning string literal",r"扫读字符串文本时遇到了EOL行结尾"),
                                        ("unexpected EOF while parsing",r"在解析过程中遇到意料之外的EOF文件结尾"),
                                        ("expression too long",r"表达式太长"),
                                        ("unexpected character after line continuation character",r"在换行继续符（\）之后遇到意料之外的字符"),
                                        ("invalid character in identifier",r"在标识符中有无效字符"),
                                        ("multiple statements found while compiling a single statement",r"在编译一个语句时发现了多条语句"),
                                        ]},
                  'NameError':{
                               'name':'名字错误',
                               'messages':[("name '%.200s' is not defined",r"名字'\1'还没有定义")
                                         ]},
                  'TabError':{
                               'name':'制表符错误',
                               'messages':[("inconsistent use of tabs and spaces in indentation",r"缩进时不一致地使用了制表符和空格"),
                                         ]},
                  'IndentationError':{
                               'name' :'缩进错误',
                               'messages':[ ("expected an indented block",r"该语句块应该缩进"),
                                            ("unexpected indent",r"此处不应该缩进"),
                                            ("unexpected unindent",r"此处不应该向前减少缩进"),
                                            ("unindent does not match any outer indentation level",r"向前减少缩进后不能与任何外层代码匹配"),
                                            ("too many levels of indentation",r"缩进层次太多"),
                                ]},
                  'TypeError':{
                               'name':'类型错误',
                               'messages':[("unsupported operand type(s) for %.100s: '%.100s' and '%.100s'", r"类型‘\2’和‘\3’之间不支持 \1 操作"),
                                         ("can only concatenate list (not \"%.200s\") to list", r'''列表只能连接列表（不能是"\1"）'''),
                                         ("can only concatenate tuple (not \"%.200s\") to tuple", r'''元组只能连拉元组（不能是"\1"）'''),
                                         ("'%.200s' object does not support item assignment", r'''‘\1’对象不支持对其中的项目赋值''')
                                         ]},
                  'KeyError':{
                               'name':'键错误',
                               'messages':[]},
                  'IndexError':{
                               'name':'索引错误',
                                'messages':[("%s assignment index out of range", r"对\1的赋值操作索引超出了范围"),
                                         ("%s index out of range", r"对\1的索引超出了范围")
                                        ]},
                  'ValueError':{
                               'name':'值错误',
                               'messages':[("invalid literal for int() with base %d: %R", r"给int()函数传递的\1进制数字写法有误：\2")]},
                  'AssertionError': {'name':'断言错误',
                               'messages':[("", r"")
                                         ]},
                  'Traceback':{
                               'name' :'回溯追踪（最近的调用在最后）',
                               'messages':[]},
                  }
