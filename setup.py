#!/usr/bin/env python
# encoding: utf-8
'''
'''

from distutils.core import setup
from dub.resource import VERSION
def install():
    setup(name = 'dub',
          version = VERSION,
          packages = ['dub'],
          author = 'Terry Yin',
          author_email = 'terry.yinze@gmail.com',
          url= 'https://github.com/terryyin/pythonTranslator',
          scripts=['dubShell.py']
          )

if __name__ == "__main__":
    install()