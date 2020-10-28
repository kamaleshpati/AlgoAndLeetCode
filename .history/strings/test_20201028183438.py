import json

with open('./foodyo_output.json') as f:
  data = json.load(f)
  for i in data['body']['Recommendations']:
      print(i['RestaurantName'])
      print('\n')
      for j in i['menu']:
          if(j['type'] is 'sectionheader'):
              for k in j['children']:
                  if k['type'] is 'item' and k['selected'] is 1:
                      print(k['name'])
                      for l in k['children']:
                          if l['selected'] is 1:
                              print(l['name'])

