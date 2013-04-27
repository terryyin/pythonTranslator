#!/usr/bin/env python
# encoding: utf-8
'''
'''

from distutils.core import setup
from dub_src.resource import VERSION, RESOURCE_FOLDER
def install():
    setup(name = 'dub',
          version = VERSION,
          package_dir = {'dub':'dub_src'},
          packages = ['dub'],
          author = 'Terry Yin',
          author_email = 'terry.yinze@gmail.com',
          url= 'https://github.com/terryyin/pythonTranslator',
          scripts=['dubShell.py'],
          data_files = [(RESOURCE_FOLDER, ['README.md'])]
          )

if __name__ == "__main__":
    install()