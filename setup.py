#!/usr/bin/env python
# encoding: utf-8
'''
'''

from distutils.core import setup
from resource import VERSION
def install():
    setup(name = 'dub',
          version = VERSION,
          py_modules = ['dub'],
          author = 'Terry Yin',
          author_email = 'terry.yinze@gmail.com',
          url= 'https://github.com/terryyin/pythonTranslator',
          scripts=['dub.py', 'dubShell.py', 'resource.py']
          )

if __name__ == "__main__":
    install()