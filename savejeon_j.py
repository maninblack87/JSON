import json

d = dict()
d['id'] = 1
d['name'] = 'Jeon'
d['hobby'] = ['yutube', 'walking', 'sobbering', 'sonic']
d['test'] = True

if not file_path:

    file_path = 'c:/jeon/json/savejson_j.json'

    with open(file_path, 'w', encoding='UTF-8')as fp:
        dumping = json.dump(d, fp, indent=4)

if file_path:

    file_path = 'c:/jeon/json/savejson_j.json'

    with open(file_path, 'r')as fp:
        data = json.load(fp)

    data["test"] = False
    data["hobby"] = data["hobby"]+["smart phone"]

    with open(file_path, 'w', encoding='utf-8')as fp:
        json.dump(data, fp, indent=4)