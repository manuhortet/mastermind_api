import json
import flask_restful

from unittest import TestCase


class TestServer(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_new_game(self):
        res = self.app.get('/new_game')
        self.assertEqual(res.status, '201 CREATED')

    def test_new_guess(self):
        data = ["BLUE", "BLUE", "BLUE", "BLUE"]
        self.app.get('/new_game')
        res = self.app.put('/new_guess', data=json.dumps(data))
        self.assertEqual(res.status, '200 OK')

    def test_bad_formated_new_guess(self):
        data = ["BLUE"]
        self.app.get('/new_game')
        res = self.app.put('/new_guess', data=json.dumps(data))
        self.assertEqual(res.status, '400 BAD REQUEST')

    def test_history_request(self):
        res = self.app.get('/history')
        self.assertEqual(res.status, '200 OK')
