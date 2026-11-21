MOVIE RECOMMENDER SYSTEM
EDA-SEARCH ENGINE-CONTENT BASED FILTERING-

BUILD A CONTENT BASED RECOMMENDER SYSTEM USING COSINE VECTORIZATION, DONE DATA PREPREOCESSING AND EDA AFTER THAT TRAINED THE DATA AND THE FETCHED THE API KEY TO USE IN THE STREAMLIT CODE

<img width="739" height="759" alt="image" src="https://github.com/user-attachments/assets/59275bea-454c-48d7-a757-ddeaf27d861c" />

<img width="1131" height="724" alt="image" src="https://github.com/user-attachments/assets/2b83f818-eb1f-4efc-862a-1767746f1705" />




## Poster configuration

Set the `TMDB_API_KEY` environment variable to your own TMDB API key before running `streamlit run app.py`. In PowerShell, use `$env:TMDB_API_KEY="your-key"`; in bash, use `export TMDB_API_KEY="your-key"`. Without a key, recommendations still display their titles. Missing artwork and failed API requests display "Poster unavailable". Each poster request has a five-second timeout.

## Regression tests

Run `python -m unittest discover -s tests -v`. Poster tests mock network calls and require only `requests`; no API key or model artifacts are needed.
