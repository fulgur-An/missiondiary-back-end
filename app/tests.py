from django.test import TestCase


class ViewsTestCase(TestCase):
  def test_index_loads_properly(self):
    """The index page loads properly"""
    response = self.client.post('localhost:8000/api/login/',
    data={
      "password": "Qwer1234",
      "user_name": "antony"
    },
    content_type='application/json')
    self.assertEqual(response.status_code, 200)