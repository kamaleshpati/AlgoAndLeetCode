import json

with open('./foodyo_output.json') as f:
  data = json.load(f)
  print(data['body']['Recommendations'])
