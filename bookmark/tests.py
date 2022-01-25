from django.test import TestCase
class TestCase(TestCase):
    def test_of_test(self):
        """Testing how to test"""
        self.assertEqual('I should fail', 'Please fix me!')