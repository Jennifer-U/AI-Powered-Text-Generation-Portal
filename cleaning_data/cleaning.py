import re
from langdetect import detect, detect_langs


input_file = 'corrupt_movie_corpus.txt'
output_file = 'cleaned_text_file.txt'


def read_file(input_file):
    with open(input_file, 'r') as file:
        return file.read() 


# Reads full file
content = read_file(input_file)


def print_lines(str, n):
    lines = str.splitlines()
    for i in range(min(n, len(lines))): # Bounds check
        print(lines[i])


def count_lines(str):
    lines = str.splitlines()
    return len(lines)  
    

def clean(content, output_file):
    cleaned_content = content

    # Defined punctuation to keep
    punctuation_maintained = ".,!?;:'\"-" 

    # Regex patterns- removes consecutive repeated words & characters not in punctuation 
    duplicate_pattern = r"\b(\w+)(?:\W+\1\b)+"
    pattern = r"[^a-zA-Z0-9\s" + re.escape(punctuation_maintained) + r"]"
   
    # Removes all tags 
    cleaned_content = re.sub(r'<.*?>', '', cleaned_content)

    # Removes URL 
    cleaned_content = re.sub(r'http[s]?://\S+', '', cleaned_content)

    # Removes special charaters not in punctuation pattern
    cleaned_content = re.sub(pattern, '', cleaned_content)

    # Removes leading digit from each line
    cleaned_content = re.sub(r"^\d+", "", cleaned_content, flags=re.MULTILINE)

    # Removes ending digit from each line
    cleaned_content = re.sub(r'\d+$', '', cleaned_content, flags=re.MULTILINE)

    # Removes consecutive repeated words
    cleaned_content = re.sub(duplicate_pattern, r'\1', cleaned_content, flags=re.IGNORECASE)
 
    # Normalize whitespace -Replacing multiple whitespaces and tabs with single space. Maintains newlines
    cleaned_content = re.sub(r'[ \t]+', ' ', cleaned_content)
    
    # Split into lines. Removing leading and trailing whitespace. Joined back together
    lines = cleaned_content.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    cleaned_content = '\n'.join(lines)

    with open(output_file, 'w') as file:
        file.write(cleaned_content)


# Phase 1: Data Analysis 
print("Inspect the following 10 lines of corrupted file sample text for identification of noise pattern:\n")
print_lines(content, 10)
print()

print("Noise patterns identified:")
print("- HTML tags \n- URLs \n- Standalone noise symbols ($, #, *, @) \n- Numbers at end or beginning of sentences")
print("- Inconsistent use of whitespaces \n- Spelling errors\n")

language = detect(content)
print(f"Primary language in this text: {language}\n")
print(f"Total Lines: {count_lines(content)}\n")


# Phase 2: Data Cleaning
clean(content, output_file)
cleaned = read_file(output_file)
print("Cleaned Data Sample: ")
print_lines(cleaned, 5)