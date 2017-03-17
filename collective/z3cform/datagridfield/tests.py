# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield.testing import FUNCTIONAL_TESTING
from plone.testing import layered

import doctest
import pprint
import unittest2 as unittest


OPTIONFLAGS = (
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE |
    doctest.REPORT_ONLY_FIRST_FAILURE
)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(
            doctest.DocFileSuite(
                'browser.txt',
                package='collective.z3cform.datagridfield',
                optionflags=OPTIONFLAGS,
                globs={'pprint': pprint.pprint, }
            ),
            layer=FUNCTIONAL_TESTING
        )
    ])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
