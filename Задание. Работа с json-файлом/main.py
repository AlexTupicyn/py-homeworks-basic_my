

import json
from collections import Counter

with open('newsafr.json', encoding='utf-8') as f:
    res = json.load(f)
    res_list = res['rss']['channel']['items']
    text_list = []
    text_list_1 = []
    for el in res_list:
        text_list = el['description'].split()
        for li in text_list:
            if len(li) > 6:
                text_list_1.append(li)
                cnt = Counter(text_list_1)
            dict_file = sorted(dict(cnt).items(), key=lambda x: x[1], reverse=True)
            dict_sort = dict(dict_file)
        #print(dict_sort)
popular = []
for key, value in dict_sort.items():
    popular.append(key)
print(popular[:10])