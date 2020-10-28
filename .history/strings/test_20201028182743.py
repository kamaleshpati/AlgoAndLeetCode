import json

with open('./foodyo_output.json') as f:
  data = json.load(f)
  for i in (data['body']['Recommendations']):
      print(i['RestaurantName'])
      print('\n')
      for j in range(i['menu']):
          if(j['type'] is 'sectionheader'):
              for k in j['children']
