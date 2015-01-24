from quicklock.quicklock import singleton
import time
from unittest import TestCase

class SingletonTestCase(TestCase):
    def test(self):

        try:
            singleton('resource')
            print('>> Test Note: Lock has been acquired, waiting for 60 seconds')
            print('>> Test Note: Run multiple instances of make test simultaneously to test operation')
            time.sleep(60)
            print('>> Test Note: Quitting and releasing lock')

        except RuntimeError, exc:
            print('>> Test Note: Lock was already in use')
            self.assertTrue(isinstance(exc, RuntimeError))
            self.assertTrue('Resource <resource> is currently locked by' in exc.message)
