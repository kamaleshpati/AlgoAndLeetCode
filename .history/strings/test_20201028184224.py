import json

def printBody(data):
    if data['selected'] != None and data['selected'] == 1:
        print(data['name'])
        if len(data['children']) != 0 or data['children'] != None:
            printBody(data['children'])



with open('./foodyo_output.json') as f:
  data = json.load(f)
  for i in data['body']['Recommendations']:
      print(i['RestaurantName'])
      print('\n')
      for j in i['menu']:
          if(j['type'] == 'sectionheader'):
              for k in j['children']:
                  if k['type'] == 'item' and k['selected'] == 1:
                      print(k['name'])
                      for l in k['children']:
                          if l['selected'] == 1:
                              print(l['name'])
                              printBody(l['children'])

