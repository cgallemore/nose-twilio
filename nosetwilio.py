import unittest
from nose.plugins.base import Plugin

class TwilioTestCase(unittest.TestCase):
    """
    Use this test case for all tests involving Twilio. This enables use to
    only run these tests if --twilio-select is used when running the tests.
    """
    pass

class NoseTwilio(Plugin):
    """
    Activate this plugin to run only test cases that extend TwilioTestCase.  By
    default, these test cases are skipped.
    """

    enabled = True
    name = "twilio-filtering"

    def options(self, parser, env):
        parser.add_option("--twilio-select",
                          dest="run_twilio_tests",
                          action="store_true",
                          default=False,
                          help="Run all TwilioTestCase tests and only them.")

    def configure(self, options, conf):
        self.run_twilio = True if options.run_twilio_tests else False

    def wantClass(self, cls):
        if self.run_twilio:
            return issubclass(cls, TwilioTestCase)
        else:
            if issubclass(cls, TwilioTestCase):
                return False

        return None