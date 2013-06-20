#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import idlelib.PyShell
    idlelib.PyShell.PyShell.menu_specs[0] = ("file", "文件")
    idlelib.PyShell.main()

if __name__ == '__main__':
    # start up IDLE with IdleX
    main()

