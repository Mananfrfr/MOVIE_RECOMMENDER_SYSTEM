"""Optional TMDB artwork; recommendations still work without network access."""
import requests


def fetch_poster(movie_id, api_key):
    """Return a poster URL, or None when credentials/artwork are unavailable."""
    if not api_key:
        return None
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}",
            params={"api_key": api_key, "language": "en-US"},
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None
    path = data.get("poster_path") if isinstance(data, dict) else None
    if not isinstance(path, str) or not path.startswith("/") or path.startswith("//"):
        return None
    return "https://image.tmdb.org/t/p/w500" + path
