from django.test import TestCase


class HomePageTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')
        self.html = self.response.content.decode('utf8')

    def test_home_page_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_home_page_correct_html(self):
        self.assertTemplateUsed(self.response, "index.html")
        self.assertIn("<title>Buying Cheap</title>", self.html)
