import os

current = os.getcwd()
folder_name = 'sorted'
path = os.path.join(current, folder_name)

def merge_sort_file(dir):
    list_file = os.listdir(path)
    dict_file = {}
    for i in range(len(list_file)):
        with open(os.path.join(current, folder_name, list_file[i]), 'rt', encoding='utf-8') as file:
            content = file.readlines()
            dict_file[list_file[i]] = content
    sort_dict = sorted(dict_file.items(), key=lambda x: len(x[1]))
    with open('result_file.txt', 'a', encoding='utf-8') as file:
        for line in sort_dict:
            file.writelines([line[0], '\n'])
            file.writelines([str(len(line[1])), '\n'])
            file.writelines(line[1])
            file.writelines('\n')

merge_sort_file(path)