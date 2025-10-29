## Project Goal
Develop a locally-run text generation application trained on real-world data.

## Part One: Data Cleaning
Clean and standardize the noisy dataset `corrupt_movie_corpus.txt` containing HTML tags, URLs, excessive punctuation, and special characters.

### Phase 1: Data Analysis
Analyze raw data to determine:
- **Size & Language**: Total line count and primary language
- **Noise Patterns**: Inspect at least 10 sample lines to identify corruption types (URLs, HTML tags, repeated punctuation)

### Phase 2: Data Cleaning
Using Python's `re` package, implement:
- **HTML Tag Removal**: Strip all tags using `<.*?>`
- **URL Removal**: Remove http://, https://, and www\. addresses
- **Character Cleanup**: Remove non-alphanumeric symbols identified during analysis
- **Whitespace Normalization**: Collapse multiple spaces into single spaces

### Deliverables
- Data Analysis phase results
- 5 sample lines of cleaned text

## Part Two: Coming Soon