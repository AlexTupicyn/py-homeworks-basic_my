import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml")
root = tree.getroot()
news_list = root.findall("channel/item/description")
text_list = []
text_list_1 = []

for row in news_list:
    res_list = row.text.split()
    for li in res_list:
        if len(li) > 6:
            text_list_1.append(li)
            cnt = Counter(text_list_1)
        dict_file = sorted(dict(cnt).items(), key=lambda x: x[1], reverse=True)
        dict_sort = dict(dict_file)
popular = []
for key, value in dict_sort.items():
    popular.append(key)
print(popular[:10])