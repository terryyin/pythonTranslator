'''
by terry.yinzhe@gmail.com
'''

import unittest

from subprocess import Popen, PIPE
import os
import resource

class testDubForPythonInInteractiveMode(unittest.TestCase):
    def setUp(self):
        env = os.environ.copy()
        env["PYTHONSTARTUP"] = "./dubShell.py"
        self.shell = Popen("python -i".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE, env = env)
        
    def testShouldSeeWelcomeInformation(self):
        stdout, stderr = self.shell.communicate("")
        self.assertIn(resource.WELCOME + resource.VERSION, stderr.splitlines())
        self.assertEqual('', stdout)
        
    def testShouldSeeTranslatedSyntaxError(self):
        stdout, stderr = self.shell.communicate("1+\n")
        self.assertIn(resource.ExceptionTypes['SyntaxError'], stderr.splitlines())
        self.assertEqual('', stdout)
        
    def testShouldNotSeeTranslatedSyntaxErrorWhenNoInput(self):
        stdout, stderr = self.shell.communicate("")
        self.assertNotIn(resource.ExceptionTypes['SyntaxError'], stderr.splitlines())
        self.assertEqual('', stdout)

class testDubForPythonInProgramMode(unittest.TestCase):
    def testShouldSeeNoErrorWhenEverythingIsOK(self):
        self.shell = Popen("python example.py".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE)
        stdout, stderr = self.shell.communicate("")
        self.assertEqual([], stderr.splitlines())
        
    def testShouldSeeTranslationOfTheError(self):
        self.shell = Popen("python example.py 1+\n".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE)
        stdout, stderr = self.shell.communicate("")
        self.assertIn(resource.ExceptionTypes['SyntaxError'], stderr.splitlines())
        
        
if __name__ == '__main__':
    unittest.main()