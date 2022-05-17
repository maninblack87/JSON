import json

d = dict()
d['id'] = 1
d['name'] = 'Jeon'
d['hobby'] = ['yutube', 'walking', 'sobbering', 'sonic']
d['test'] = True

file_path = 'c:/jeon/json/savejson.json'

with open(file_path, 'w', encoding='UTF-8')as fp:
    json.dump(d, fp, indent=4)
