import config
import re
import requests
from datetime import datetime
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

def scrape_url(url, words_frequency):
    URL='https://'+url
    print(URL)
    try:
        res = requests.get('https://'+url, headers=config.requestHeaders, timeout=15)
        if res.status_code !=200 :
            res=requests.get('http://'+url, headers=config.requestHeaders, timeout=15)
        if res.status_code ==200 :
            soup = BeautifulSoup(res.text, "html.parser")
            [tag.decompose() for tag in soup("script")]
            [tag.decompose() for tag in soup("style")]
            text = soup.get_text()
            cleaned_text = re.sub('[^a-zA-Z]+', ' ', text).strip()
            tokens = word_tokenize(cleaned_text)
            tokens_lemmatize = remove_stopwords(tokens)
            return predict_category(words_frequency, tokens_lemmatize)
        else:
            print('Something went wrong')
    except Exception as e:
        print(f'Error code:\n {e}')
        return False


def predict_category(words_frequency, tokens):
    category_weights = []
    for category in words_frequency:
        weight = 0
        intersect_words = set(words_frequency[category]).intersection(set(tokens))
        for word in intersect_words:
            if word in tokens:
                index = words_frequency[category].index(word)
                weight += config.words - index
        category_weights.append(weight)

    category_index = category_weights.index(max(category_weights))
    main_category = list(words_frequency.keys())[category_index]
    category_weights[category_index] = 0

    category_index = category_weights.index(max(category_weights))
    main_category_2 = list(words_frequency.keys())[category_index]
    
    return main_category, main_category_2


def timeit(start):
    stop = datetime.now()
    return stop - start


def remove_stopwords(tokens):
    tokens_list = []
    for word in tokens:
        word = wnl.lemmatize(word.lower())
        if word not in config.stopWords:
            tokens_list.append(word)
    return list(filter(lambda x: len(x) > 1, tokens_list))


def scrape(props):
    i = props[0]
    url = props[1]
    print(i, url)
    try:
        return requests.get(url, headers=config.requestHeaders, timeout=15)
    except:
        return ''


def parse_request(props):
    i = props[0]
    res = props[1]
    if res != '' and res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        [tag.decompose() for tag in soup("script")]
        [tag.decompose() for tag in soup("style")]
        text = soup.get_text()
        cleaned_text = re.sub('[^a-zA-Z]+', ' ', text).strip()
        tokens = word_tokenize(cleaned_text)
        tokens_lemmatize = remove_stopwords(tokens)
        return (i, tokens_lemmatize)
    else:
        return (i, [''])
