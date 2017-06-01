import abc
import inspect
import re
import unittest
from json import load


class TestCaseWithFixtures(unittest.TestCase):
    __metaclass__ = abc.ABCMeta

    def __init__(self, method_name='runTest'):
        super(TestCaseWithFixtures, self).__init__(method_name)
        self._load_fixtures()

    def _get_data(self):
        """Provides fixture data for caller method

        :return: fixture data
        :rtype: any
        """
        caller_name = inspect.stack()[1][3]
        if caller_name in self.__data:
            return self.__data[caller_name]
        return {}

    def _load_fixtures(self):
        """Loads fixtures from json file with the same name as current test file and puts it into __data property

        :return:
        """
        filename = inspect.getfile(self.__class__)
        filename = re.sub('\.(py|pyc).*$', '', filename)
        try:
            with open('%s.json' % filename, 'r') as fp:
                self.__data = load(fp)
        except IOError as e:
            self.__data = {}
