import json
import pandas as pd

data_csv = pd.DataFrame({'link': [],
                         'title': [],
                         'description': [],
                         'content': [],
                         'category': [],
                         'pub_date': [],
                         'keywords': [],
                         'tag': [],
                         })
if __name__ == "__main__":
    f = open('vnexpress3_20200817_012505.json', 'r', encoding='utf-8')
    data = f.read().split('\n')
    # print(data[0])
    for item in data:
        temp = json.loads(item)
        x = json.loads(json.dumps(temp))
        data_csv = data_csv.append({'link': x['link'],
                                    'title': x['title'],
                                    'description': x['description'],
                                    'content': x['content'],
                                    'category': x['category'],
                                    'pub_date': x['pub_date'],
                                    'keywords': x['keywords'],
                                    'tag': x['tags']}, ignore_index=True)

        data_csv.to_csv('data.csv', encoding='utf-8')

