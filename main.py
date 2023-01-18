import pickle
import config
import argparse
from functions import scrape_url


def x(url):
    pickle_in = open(config.wfPath, "rb")
    wf = pickle.load(pickle_in)

    if url:
        print(url)
        results = scrape_url(url, wf)
        if results:
            return results
