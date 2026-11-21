"""Rank candidates by row position, excluding the selected movie explicitly."""


def recommendation_indices(scores, selected_index, limit=5):
    if not 0 <= selected_index < len(scores):
        raise ValueError("Selected movie index is outside the similarity row")
    if limit < 0:
        raise ValueError("Recommendation limit cannot be negative")
    candidates = (i for i in range(len(scores)) if i != selected_index)
    return sorted(candidates, key=lambda i: scores[i], reverse=True)[:limit]
