import sys
sys.path.append("..")

import unittest
from config import MostViewedArticles_uri, ViewCountPerArticle_uri

class Test_MostViewedArticles_uri(unittest.TestCase):
    def test_config_urls_weekly(self):
        actual_url = MostViewedArticles_uri().get_url_for_mostview_weekly(2020,10,2)
        expected_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/2020/10/2"
        self.assertTrue(actual_url, expected_url)
        
    def test_config_urls_monthly(self):
        actual_url = MostViewedArticles_uri().get_url_for_mostview_monthly(10,2)
        expected_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/10/2/all-days"
        self.assertTrue(actual_url, expected_url)

class Test_ViewCountPerArticle_uri(unittest.TestCase):
    def test_config_urls_weekly_or_monthly(self):
        actual_url = ViewCountPerArticle_uri().get_url_for_viewcount_monthly_or_weekly("Alert Einstein","2020100100","2020103000")
        expected_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Alert Einstein/daily/2020100100/2020103000"
        self.assertTrue(actual_url, expected_url)



if __name__ == '__main__':
    unittest.main()