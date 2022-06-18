import xml.etree.ElementTree as ET
types_txtfile = set()
types_xmlfile = set()

with open('games.txt') as file:
     record = file.readline()
     while record:
         fields = record.rstrip().split(',')
         type_game = fields[-5].strip("'").strip(" ").lower()
         types_txtfile.add(type_game)
         record = file.readline()
print('In the txt-file:', len(types_txtfile), 'types of games')
# print(types_txtfile)

# create set with info from xml file
xmlDoc = ET.parse("games.xml")
root = xmlDoc.getroot()

for game in root.findall("game"):
    types_xmlfile.add(game[1].text.lower())

print('In the xml-file:', len(types_xmlfile), 'types of games')
# print(types_xmlfile)

print('\nThe types that occur in both files:')
print(types_txtfile & types_xmlfile)
print('\nThe types that only appear in the txt-file:')
print(types_txtfile - types_xmlfile)
print('\nThe types that only appear in the xml-file:')
print(types_xmlfile - types_txtfile)