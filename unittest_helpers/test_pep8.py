from __future__ import absolute_import

import os
import unittest

import pep8

ignore_patterns = ['.git', '.idea']


class PEPHelper(object):
    files = []

    def pep8_check(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        python_files = []
        for root, _, files in os.walk('./'):
            if self.__ignore(root):
                continue
            python_files.extend([os.path.join(root, f) for f in files if f.endswith('.py')])
        result = style.check_files(python_files)
        return result

    @staticmethod
    def __ignore(directory):
        for pattern in ignore_patterns:
            if pattern in directory:
                return True
        return False


class TestPEP8(unittest.TestCase, PEPHelper):
    def test_pep8(self):
        result = self.pep8_check()
        self.assertEqual(result.total_errors, 0, 'PEP8 validation fails. Errors count: %s' % result.total_errors)
