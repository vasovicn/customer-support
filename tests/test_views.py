from django.test import TestCase


class ViewTest(TestCase):
    def test_customer_service_homepage_view(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)


    def test_customer_service_support_view(self):
        resp = self.client.get("/support")
        self.assertEqual(resp.status_code, 200)
