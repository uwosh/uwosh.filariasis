import unittest
from Testing import ZopeTestCase as ztc

from uwosh.filariasis.tests.base import FunctionalTestCase
        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(ztc.FunctionalDocFileSuite(
                      'browser.txt', package='uwosh.filariasis.tests',
                      test_class=FunctionalTestCase))
    return suite
