import unittest
import inspect
from json import load
import os
import re
import abc

class TestCaseWithFixtures(unittest.TestCase):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.__data = None

    def setUp(self):
        self.__load_fixtures()

    def __get_data(self):
        """Provides fixture data for caller method

        :return: fixture data
        :rtype: any
        """
        caller_name = inspect.stack()[1][3]
        if caller_name in self.__data:
            return self.__data[caller_name]
        return {}

    def __load_fixtures(self):
        """Loads fixtures from json file with the same name as current test file and puts it into __data property

        :return:
        """
        filename = os.path.abspath(__file__)
        filename = re.sub('\.(py|pyc).*$', '', filename)
        try:
            with open('%s.json' % filename, 'r') as fp:
                self.__data = load(fp)
        except IOError as e:
            print e
            self.__data = {}


