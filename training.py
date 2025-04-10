import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import config
import nltk
import pickle
from functions import timeit, scrape, parse_request
from sklearn.model_selection import train_test_split

# Read and filter dataset
df = pd.read_csv(config.datasetPath)
df = df.rename(columns={'main_category:confidence': 'main_category_confidence'})
df = df[['url', 'main_category', 'main_category_confidence']]
df['dl'] = df.url.apply(lambda x: x.split('.')[-1])
df = df[df.dl.isin(config.domainWhiteList)].reset_index(drop=True)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(df['url'], df['main_category'],test_size=0.20, random_state = 0)
df=pd.concat([X_train,y_train],axis=1)

# Remove broken or non-working sites
df = df[(df['main_category'] != 'Not_working') ]

df['url'] = df['url'].apply(lambda x: 'http://' + x)

df['tokens'] = ''

if __name__ == '__main__':
    # Part 1: Download and fetch HTML using threads (multithreading)
    with ThreadPoolExecutor(config.threadingWorkers) as executor:
        start = datetime.now()
        results = executor.map(scrape, [(i, elem) for i, elem in enumerate(df['url'])])
    exec_1 = timeit(start)

    # Part 2: Parse and process HTML using multiple CPU processes (multiprocessing)
    with ProcessPoolExecutor(config.multiprocessingWorkers) as ex:
        start = datetime.now()
        res = ex.map(parse_request, [(i, elem) for i, elem in enumerate(results)])

    # Save tokenized results to dataframe
    for props in res:
        i = props[0]
        tokens = props[1]
        df.at[i, 'tokens'] = tokens
    exec_2 = timeit(start)

    # Part 3: Build frequency list of words per category
    start = datetime.now()
    words_frequency = {}
    for category in df.main_category.unique():
        print(category)
        all_words = []
        df_temp = df[df.main_category == category]
        for word in df_temp.tokens:
            all_words.extend(word)
        most_common = [word[0] for word in nltk.FreqDist(all_words).most_common(config.words)]
        words_frequency[category] = most_common 

    # Save words_frequency model
    pickle_out = open(config.wfPath, "wb")
    pickle.dump(words_frequency, pickle_out)
    pickle_out.close()

    exec_3 = timeit(start)

    print('\nPart 1: ', exec_1, '\nPart 2: ', exec_2, '\nPart 3: ', exec_3)