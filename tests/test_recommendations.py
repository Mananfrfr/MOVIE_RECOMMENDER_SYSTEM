import unittest

from recommendations import recommendation_indices


class RecommendationTests(unittest.TestCase):
    def test_tied_scores_exclude_selected_movie(self):
        self.assertEqual(recommendation_indices([1.0, 1.0, 0.5], 1), [0, 2])

    def test_self_need_not_have_highest_score(self):
        self.assertEqual(recommendation_indices([0.9, 0.4, 0.8], 1), [0, 2])

    def test_scores_sorted_descending(self):
        self.assertEqual(recommendation_indices([0.2, 1.0, 0.8, 0.5], 1), [2, 3, 0])

    def test_limit_and_stable_ties(self):
        self.assertEqual(recommendation_indices([1, 0.5, 0.5, 0.5], 0, 2), [1, 2])

    def test_small_catalog(self):
        self.assertEqual(recommendation_indices([1], 0), [])
        self.assertEqual(recommendation_indices([1, 0.5], 0), [1])

    def test_zero_limit(self):
        self.assertEqual(recommendation_indices([1, 0.5], 0, 0), [])

    def test_invalid_inputs(self):
        for scores, index, limit in [([], 0, 5), ([1], -1, 5), ([1], 1, 5), ([1], 0, -1)]:
            with self.subTest(scores=scores, index=index, limit=limit):
                with self.assertRaises(ValueError):
                    recommendation_indices(scores, index, limit)


if __name__ == "__main__":
    unittest.main()
