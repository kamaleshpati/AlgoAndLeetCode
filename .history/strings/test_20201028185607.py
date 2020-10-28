import json

def printBody(data):
    if data['selected'] != None and data['selected'] == 1:
        print('---->',end="")
        print(data['name'])
        if len(data['children']) != 0 or data['children'] != None:
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
                            printBody(l)




# result

# palace restaurant
# -->hamburger
# ---->meal additions
# sherwood to go
# -->hamburger
# ---->choice of burger
# ---->beef burger
# corner grocers
# -->hamburger
# ---->choice of meat preparation
# ---->well done
# panini grill
# -->beef burger
# ---->pick one
# ---->single (6 oz)
# cozy corner
# -->beef burger
# ---->pick one
# ---->sandwich
# america's burgers & wraps
# -->beef burger
# ---->burger extras
# space 62 market
# --> hamburger
# ---->protein add-ons
# midtown diner & restaurant
# -->hamburger club triple decker
# ---->choice of meat preparation
# ---->medium rare
# ritz diner
# -->american style burger
# ---->pick one
# ---->regular
# trend diner
# -->john wayne burger
# ---->burger add-ons
# cafe luka
# -->california burger
# ---->burger toppings
# avenue diner
# -->greek burger
# ---->choice of condiments