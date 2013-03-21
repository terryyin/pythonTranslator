'''
by terry.yinzhe@gmail.com
'''
import resource
import sys
import traceback

def excepthook(exctype, value, tb):
    sys.stderr.writelines(traceback.format_exception(exctype, value, tb))
    sys.stderr.write(resource.ExceptionTypes['SyntaxError'] + '\n')
    
sys.excepthook = excepthook

sys.stderr.write(resource.WELCOME + resource.VERSION + "\n")
if __name__ == '__main__':
    pass