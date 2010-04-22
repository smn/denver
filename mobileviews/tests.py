from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class UserAgentTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def _do_request(self, user_agent):
        return self.client.get(reverse("mobile_view"), \
                                                HTTP_USER_AGENT=user_agent)
    
    def test_responses(self):
        for ua in ["dumb", "smart", "brilliant"]:
            response = self._do_request(ua)
            self.assertContains(response, "you're %s" % ua)
    
    def test_dumb_and_quirky(self):
        response = self._do_request("dumb; quirky")
        self.assertContains(response, "and you're quirky")
