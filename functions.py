import config
import re
import requests
from datetime import datetime
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

# Handles URL content fetching and NLP processing
def scrape_url(url, words_frequency):
    try:
        # Send HTTP request, fallback to http if https fails
        res = requests.get('https://'+url, headers=config.requestHeaders, timeout=15)
        if res.status_code !=200 :
            res=requests.get('http://'+url, headers=config.requestHeaders, timeout=15)
        if res.status_code ==200 :
            # Parse HTML, remove script and style tags
            soup = BeautifulSoup(res.text, "html.parser")
            [tag.decompose() for tag in soup("script")]
            [tag.decompose() for tag in soup("style")]
            
            # Extract and clean text
            text = soup.get_text()
            cleaned_text = re.sub('[^a-zA-Z]+', ' ', text).strip()

            # Tokenize and lemmatize
            tokens = word_tokenize(cleaned_text)
            tokens_lemmatize = remove_stopwords(tokens)

            # Predict categories based on trained word frequencies
            return predict_category(words_frequency, tokens_lemmatize)
        else:
            print('Something went wrong')
    except Exception as e:
        print(f'Error code:\n {e}')
        return False

# Predict the top 2 categories based on word frequency matching
def predict_category(words_frequency, tokens):
    category_weights = []
    for category in words_frequency:
        weight = 0
        # Compare input tokens with known high-frequency words per category
        intersect_words = set(words_frequency[category]).intersection(set(tokens))
        for word in intersect_words:
            if word in tokens:
                index = words_frequency[category].index(word)
                weight += config.words - index # Higher-ranked words have more weight
        category_weights.append(weight)

    # Get top 2 category predictions
    category_index = category_weights.index(max(category_weights))
    main_category = list(words_frequency.keys())[category_index]
    category_weights[category_index] = 0 # zero out first for second best

    category_index = category_weights.index(max(category_weights))
    main_category_2 = list(words_frequency.keys())[category_index]
    
    return main_category, main_category_2

# Helper: measure elapsed time for processing stages
def timeit(start):
    stop = datetime.now()
    return stop - start

# Lemmatize, lowercase and filter stopwords
def remove_stopwords(tokens):
    tokens_list = []
    for word in tokens:
        word = wnl.lemmatize(word.lower())
        if word not in config.stopWords:
            tokens_list.append(word)
    return list(filter(lambda x: len(x) > 1, tokens_list)) # remove short tokens

# Given an index and a URL, make a request and return the response object.
# Used in the multithreaded section of training.py to fetch many URLs in parallel.
def scrape(props):
    i = props[0]
    url = props[1]
    print(i, url)
    try:
        # Send an HTTP request with headers to avoid being blocked by servers
        return requests.get(url, headers=config.requestHeaders, timeout=15)
    except:
         # If the request fails (timeout, DNS error, etc.), return empty string
        return ''

# Given an index and an HTTP response, extract and clean visible text from HTML,
# then tokenize and remove stopwords. This is CPU-bound and runs with multiprocessing.
def parse_request(props):
    i = props[0]
    res = props[1]
    if res != '' and res.status_code == 200:
        # Parse HTML and remove unwanted tags
        soup = BeautifulSoup(res.text, "html.parser")
        [tag.decompose() for tag in soup("script")]
        [tag.decompose() for tag in soup("style")]

        # Extract and clean all visible text
        text = soup.get_text()
        cleaned_text = re.sub('[^a-zA-Z]+', ' ', text).strip()

        # Tokenize the text and lemmatize
        tokens = word_tokenize(cleaned_text)
        tokens_lemmatize = remove_stopwords(tokens)

        # Return index and processed tokens
        return (i, tokens_lemmatize)
    else:
        # If response failed, return empty token list
        return (i, [''])
