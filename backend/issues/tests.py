"""Tests to ensure that issues endpoint works properly."""
from django.test import TestCase

from rest_framework.test import APIClient


class IssueApiTestCase(TestCase):
    """
    Testcase for issue api CRUD.
    """

    def setUp(self):
        """
        Initial setup to perform the tests.
        """
        self.client = APIClient()

    def test_issue_get(self):
        """
        Make sure that when a get is made, the status code returns 200.
        """
        response = self.client.get('/api/issues/')
        response_content = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)

    def test_issue_post(self):
        """
        Make sure that when a correct post is made, the status code returns 201.
        """
        payload = {
            "title": "new issue",
            "description": "testing this post",
        }
        response = self.client.post("/api/issues/", data=payload, format="json"
        )
        self.assertEqual(response.status_code, 201)
