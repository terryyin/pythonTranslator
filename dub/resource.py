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
                                 'detail':[("invalid syntax",r""),
                                        ("invalid token",r'无效的语法'),
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
                               'detail':[("name '%.200s' is not defined",r"名字'\1'还没有定义")
                                         ]},
                  'TabError':{
                               'name':'制表符错误',
                               'detail':[("inconsistent use of tabs and spaces in indentation",r"缩进时不一致地使用了制表符和空格"),
                                         ]},
                  'IndentationError':{
                               'name' :'缩进错误',
                               'detail':[ ("expected an indented block",r"该语句块应该缩进"),
                                            ("unexpected indent",r"此处不应该缩进"),
                                            ("unexpected unindent",r"此处不应该向前减少缩进"),
                                            ("unindent does not match any outer indentation level",r"向前减少缩进后不能与任何外层代码匹配"),
                                            ("too many levels of indentation",r"缩进层次太多"),
                                ]},
                  'TypeError':{
                               'name':'类型错误',
                               'detail':[("unsupported operand type(s) for %.100s: '%.100s' and '%.100s'", r"类型‘\2’和‘\3’之间不支持 \1 操作")
                                         ]},
                  'AssertionError': {'name':'断言错误',
                               'detail':[("", r"")
                                         ]},
                  'Traceback':{
                               'name' :'回溯追踪（最近的调用在最后）',
                               'detail':[('','')]},
                  }
