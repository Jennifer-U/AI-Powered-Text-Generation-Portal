Project Goal

This project aims to clean and standardize a noisy textual dataset, corrupt_movie_corpus.txt. The file is intentionally corrupted with common web-scraping noise, including HTML tags, URLs, excessive punctuation, and special characters.

Phase 1: Data Analysis (Exploration)
Before cleaning, analyze the raw data to determine the following:

Size & Language: Determine the total line count and the primary language used.

Noise Patterns: Inspect at least 10 sample lines to identify and document all forms of corruption present (URLs, specific HTML tags like <p> or <br>, and random/repeated punctuation).

Phase 2: Data Cleaning
The Python script must execute the following essential cleaning steps, utilizing the re package (RegEx) for pattern matching. 
HTML Tag Removal: Use Regular Expressions (re) to strip all structural HTML/XML tags (<.*?>).

URL Removal: Remove all web addresses (http://, https://, www.).

Emoji Handling: Look up and apply a method (like the emoji package or specific RegEx) to remove any non-textual emoji characters.

Character and Symbol Cleanup: Remove miscellaneous, non-alphanumeric symbols and redundant characters identified during exploration (e.g., &amp;).

Whitespace Normalization: Use RegEx to compress multiple spaces into a single space between words.

Final Deliverables
The output of the completed Python script must include:

Cleaned Data Samples: Print 5 sample lines of the final, cleaned text.
