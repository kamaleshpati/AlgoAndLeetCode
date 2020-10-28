import json

def printBody(data):
    if data['selected'] != None and data['selected'] == 1:
        print('---->',end="")
        print(data['name'])
        if len(data['children']) != 0 or data['children'] != None:
            print('-->',end="")
            for m in data['children']:
                printBody(m)



with open('./foodyo_output.json') as f:
  data = json.load(f)
  for i in data['body']['Recommendations']:
      print(i['RestaurantName'])
      for j in i['menu']:
          if(j['type'] == 'sectionheader'):
              for k in j['children']:
                  if k['type'] == 'item' and k['selected'] == 1:
                      print('-->',end="")
                      print(k['name'])
                      for l in k['children']:
                          if l['selected'] == 1:
                              printBody(l)

