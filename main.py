import pickle
import config
import argparse
from functions import scrape_url

# Entry point for category prediction. Takes a URL and returns two most likely categories.
def x(url):
    # Load trained word frequency model from pickle file
    pickle_in = open(config.wfPath, "rb")
    wf = pickle.load(pickle_in)

    if url:
        print(url)
        # Extract tokens from the given URL and predict categories
        results = scrape_url(url, wf)
        if results:
            return results
