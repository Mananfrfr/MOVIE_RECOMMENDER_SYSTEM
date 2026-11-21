import unittest
from unittest.mock import Mock, patch

import requests
from posters import fetch_poster


class PosterTests(unittest.TestCase):
    @patch("posters.requests.get")
    def test_no_key_skips_network(self, get):
        self.assertIsNone(fetch_poster(1, ""))
        get.assert_not_called()

    @patch("posters.requests.get")
    def test_success_uses_timeout_and_params(self, get):
        get.return_value = Mock(json=Mock(return_value={"poster_path": "/image.jpg"}))
        self.assertEqual(fetch_poster(42, "test-key"), "https://image.tmdb.org/t/p/w500/image.jpg")
        get.assert_called_once_with("https://api.themoviedb.org/3/movie/42",
                                    params={"api_key": "test-key", "language": "en-US"}, timeout=5)
        get.return_value.raise_for_status.assert_called_once()

    @patch("posters.requests.get")
    def test_unavailable_artwork(self, get):
        for payload in ({}, {"poster_path": None}, {"poster_path": 3}, [],
                        {"poster_path": ""}, {"poster_path": "//invalid"}):
            with self.subTest(payload=payload):
                get.return_value = Mock(json=Mock(return_value=payload))
                self.assertIsNone(fetch_poster(1, "test-key"))

    @patch("posters.requests.get")
    def test_request_failures(self, get):
        for error in (requests.Timeout(), requests.ConnectionError()):
            get.side_effect = error
            self.assertIsNone(fetch_poster(1, "test-key"))

    @patch("posters.requests.get")
    def test_http_error(self, get):
        get.return_value.raise_for_status.side_effect = requests.HTTPError()
        self.assertIsNone(fetch_poster(1, "test-key"))
        get.return_value.json.assert_not_called()

    @patch("posters.requests.get")
    def test_invalid_json(self, get):
        get.return_value.json.side_effect = ValueError("invalid JSON")
        self.assertIsNone(fetch_poster(1, "test-key"))


if __name__ == "__main__":
    unittest.main()
