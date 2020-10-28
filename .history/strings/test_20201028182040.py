import json

with open('./foodyo_output.json') as f:
  data = json.load(f)
  for i in (data['body']['Recommendations']):
      print(i['RestaurantName'])
      print('\n')
