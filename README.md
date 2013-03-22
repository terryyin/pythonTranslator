dub是一个Python双语化模块，它可以把大部分的Python出错信息翻译成双语输出。

＊＊＊＊＊＊注意＊＊＊＊＊＊＊
 尚在开发中，翻译内容有限
=====================================================
安装方法
-------
下载代码（用git clone或者下载zip）。
在目录下执行：
python setup.py install
如遇到错误：
sudo python setup.py install

使用方法
-------
在需要使用双语化的代码或者交互shell里输入：
import dub
这样出错信息就会变成双语的。
目前有一个限制就是如果和import dub同级的代码有语法错误，那么dub还没有开始工作，所以错误信息仍为中文。


For developer
================
To run unit test:
python -munittest test

This project is going to provide multiple language support for the Python programming language. e.g. Enable Python to output error messages in Chinese.

My current plan is to use
sys.displayhook(value)
and
sys.excepthook(type, value, traceback)
to add hooks to Python. Then probably use
$PYTHONSTARTUP
To make it default behavior of the system.

Expecting Features
----------
* catch the syntax error and translate the output
+ catch other error and translate
+ catch errors output in unittest
+ persistently change PYTHONSTARTUP and IDLE setup automatically
+ "python -mdub SyntaxError" will provide help for SyntaxError in dual language
+ build a document
