from quicklock.quicklock import singleton
import time
import traceback
from unittest import TestCase

class SingletonTestCase(TestCase):
    def test(self):
        print('# Test Note: Run multiple instances of make test simultaneously to test operation')

        try:
            singleton('resource')
            print('# Test Note: Lock has been acquired, waiting for 60 seconds')
            time.sleep(60)
            print('# Test Note: Quitting and releasing lock')

        except RuntimeError, exc:
            traceback.print_exc()
            print('# Test Note: Lock was already in use')
            self.assertTrue(isinstance(exc, RuntimeError))
            self.assertTrue('Resource <resource> is currently locked by' in exc.message)
