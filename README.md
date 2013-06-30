dub是一个Python双语化模块，它可以把大部分的Python出错信息翻译成双语输出。

＊＊＊＊＊＊注意＊＊＊＊＊＊＊
 尚在开发中，翻译内容有限
=====================================================
安装方法
-------
下载代码（用git clone或者下载zip）。

在目录下执行：
<pre>
python setup.py install
</pre>
如遇到错误：
<pre>
sudo python setup.py install
</pre>
使用方法
-------
在需要使用双语化的代码或者交互shell里输入：
<pre>
import dub
</pre>
这样出错信息就会变成双语的。目前有一个限制是如果和import dub同级的代码有语法错误，那么dub还没有开始工作，所以错误信息仍为英文。

For developer
================
To run unit test:
<pre>
python -munittest test
</pre>
This project is going to provide multiple language support for the Python programming language. e.g. Enable Python to output error messages in Chinese.

ToDo
----------
- [ ] persistently change PYTHONSTARTUP and IDLE setup automatically
- [ ] "python -mdub SyntaxError" will provide help for SyntaxError in dual language
- [ ] read from a .md document. A new interface to load a different document
- [ ] Display Chinese in error output other than '\xe5\x90...'
- [ ] Flags for output in translated language only
- [ ] Chinese display in Eclipse console
- [ ] add examples to doc
- [ ] Use translate sever to translate unknown message
- [ ] Collect unknown message and count popularity
- [ ] SyntaxError in IDLE (need to hack IDLE)

WELCOME
=====
已启动Python中英文双语插件DUB
##SyntaxError:语法错误
###invalid syntax
无效的语法
###invalid token
无效的单词
###EOF while scanning triple-quoted string literal
扫读三个引号括起的字符串文本时遇到了EOF文件结尾
###EOL while scanning string literal
扫读字符串文本时遇到了EOL行结尾
###unexpected EOF while parsing
在解析过程中遇到意料之外的EOF文件结尾
###expression too long
表达式太长
###unexpected character after line continuation character
在换行继续符（\）之后遇到意料之外的字符
###invalid character in identifier
在标识符中有无效字符
###multiple statements found while compiling a single statement
在编译一个语句时发现了多条语句
                                        
##NameError:名字错误
###name '%.200s' is not defined
名字'\1'还没有定义
                                         
##TabError:制表符错误
###inconsistent use of tabs and spaces in indentation
缩进时不一致地使用了制表符和空格
                                         
##IndentationError:缩进错误
###expected an indented block
该语句块应该缩进
###unexpected indent
此处不应该缩进
###unexpected unindent
此处不应该向前减少缩进
###unindent does not match any outer indentation level
向前减少缩进后不能与任何外层代码匹配
###too many levels of indentation
缩进层次太多
                                
##TypeError:类型错误
###unsupported operand type(s) for %.100s: '%.100s' and '%.100s'
类型‘\2’和‘\3’之间不支持 \1 操作
###can only concatenate list (not \"%.200s\") to list
列表只能连接列表（不能是"\1"）
###can only concatenate tuple (not \"%.200s\") to tuple
元组只能连接元组（不能是"\1"）
###'%.200s' object does not support item assignment
‘\1’对象不支持对其中的项目赋值
###can only concatenate list (not "%.100s") to list
列表只能和列表相连接（不能是\1）
##KeyError:键错误
                         
##IndexError:索引错误
###%s assignment index out of range
对\1的赋值操作索引超出了范围
###%s index out of range
对\1的索引超出了范围
                                        
##ValueError:值错误
###invalid literal for int() with base %d: %R
给int()函数传递的\1进制数字写法有误：\2
##AssertionError:断言错误
##Traceback:回溯追踪（最近的调用在最后）:
