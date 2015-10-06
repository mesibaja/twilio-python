# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class WorkerTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "activity_name": "available",
                "activity_sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "attributes": "{\\"email\\": \\"test@twilio.com\\", \\"phone\\": \\"8675309\\"}",
                "available": true,
                "date_created": "2014-05-14T10:50:02Z",
                "date_status_changed": "2014-05-14T23:26:06Z",
                "date_updated": "2014-05-14T23:26:06Z",
                "friendly_name": "Test Worker",
                "sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        self.twilio.taskrouter.v1.workspaces.get(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .workers.get(sid="WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        ))
