from operator import itemgetter
import xml.etree.ElementTree as ET

def menu():
     print ('List of plants, sorted by')
     print('\tA: Alphabet')
     print('\tH: Price (high to low)')
     print('\tL: Price (low to high)')
     choice = input('Your choice: ').upper()
     return choice

def fill_list_withXML():
     xmlDoc = ET.parse("plants.xml")
     root = xmlDoc.getroot()
     list=[]
     for plant in root.iter('plant'):
         plantinfo = [plant[0].text, plant[4].text] # 0=name, 4=price
         list.append(plantinfo)
     # print(list)
     return list

#main program
pricelist = fill_list_withXML()
choice = menu()

while choice not in 'AHL':
     choice = menu()

if choice == 'A':
     pricelist.sort()
elif choice == 'L':
     pricelist.sort(key=itemgetter(1))
else:
     pricelist.sort(key=itemgetter(1), reverse=True)

for item in pricelist:
     print(item[1] + ' | ' + item[0])
