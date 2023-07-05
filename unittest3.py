import unittest

from flask import Flask

from app import app


class AppRoutingTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def check_route(self, route, expected_content):
        response = self.app.get(route)
        self.assertEqual(response.status_code, 200)
        if expected_content in response.data.decode():
            return True
        else:
            return False

    def test_home_route(self):
        result = self.check_route('/home', 'Ayurveda Hospital')
        self.assertTrue(result, "Home route is not working")

    def test_about_route(self):
        result = self.check_route('/about', 'About Ayurveda Hospital')
        self.assertTrue(result, "About route is not working")

    def test_schedule_route(self):
        result = self.check_route('/shedule', 'Appointment Form')
        self.assertTrue(result, "Schedule route is not working")

    def test_payment_route(self):
        result = self.check_route('/pay', 'Payment Form')
        self.assertTrue(result, "Payment route is not working")

if __name__ == '__main__':
    unittest.main()
