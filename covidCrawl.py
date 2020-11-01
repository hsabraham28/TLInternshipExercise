import sys
from comcrawl import IndexClient
import pandas as pd

client = IndexClient(['2020-05', '2020-10', '2020-16', '2020-24', '2020-29', '2020-34', '2020-40'])
client.results = []
urlss = ['reuters.com/*', 'cnn.com/*', 'nytimes.com/*', 'bbc.com/*', 'cepr.org/*', 'economist.com/*']
for ul in urlss:
    client.results.append(client.search(ul, threads=6)) 



client.results = (pd.DataFrame(client.results)
                  .sort_values(by="timestamp")
                  .drop_duplicates("urlkey", keep="last")
                  .to_dict("records"))

client.results = [res for res in client.results if res['status'] == '200' and 'covid' in res['url'] and ('financ' in res['url'] or 'econ' in res['url'] or 'cost' in res['url'] or 'job' in res['url'])][:1000]
df = pd.DataFrame(client.results)
del df['urlkey']
del df['charset']
del df['digest']
del df['mime-detected']
del df['languages']
del df['mime']
del df['length']
del df['offset']
del df['filename']
del df['redirect']

df.to_csv("results.csv")