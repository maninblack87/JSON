import urllib.request as request
import json

json_str = request.urlopen("http://api.github.com/repositories").read()
output = json.loads(json_str)

print(type(output))
print(output)
