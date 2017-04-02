from django.test import LiveServerTestCase
from selenium import webdriver


class SearchTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_display_search_view(self):
        self.browser.get(self.live_server_url)
        self.assertEqual('YouTube', self.browser.title)
