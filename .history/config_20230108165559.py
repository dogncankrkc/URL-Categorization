from nltk.corpus import stopwords

requestHeaders = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

datasetPath = f'C:Users\PC\Desktop\webCategorization-main\Datasets\urlCategorization.csv'
wfPath = f"C:/Users/PC/Desktop/webCategorization-main/models/wordFrequency.picle"

domainWhiteList = {'com', 'net', 'to', 'info', 'org', 'cn', 'jp', 'tw', 'ir', 'uk', 'ae', 'tv', 'in', 'hk',
                              'th', 'ca', 'us', 'gr', 'ws', 'io', 'bg', 'au', 'gov', 'il', 'za', 'edu', 'me', 'ph',
                              'ag', 'bd', 'biz', 'ie', 'kr', 'asia', 'my', 'by', 'nz', 'mil', 'sg', 'kz', 'eg', 'qa',
                              'pn', 'guide', 'ke', 'bz', 'im', 'pk', 'ps', 'aero', 'ck', 'museum', 'int', 'np', 'jobs',
                              'cy', 'gg', 'bw', 'bt', 'gh', 'af', 'coop', 'zzz', 'tk'
                              }

stopWords = set(stopwords.words('english'))
with open("C:/Users/PC/Desktop/webCategorization-main/Datasets/stopwords.txt") as f:
    for word in f:
        stopWords.add(word.replace('\n', ''))

for domainTypes in (domainWhiteList - {'museum', 'jobs', 'guide', 'aero'}):
    stopWords.add(domainTypes)

words = 20000
threadingWorkers = 16
multiprocessingWorkers = 6