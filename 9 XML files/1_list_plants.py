import xml.etree.ElementTree as ET
xmlDoc = ET.parse("plants.xml")
root = xmlDoc.getroot()
counter = 1

# exercise a)
# for plant in root.findall('plant'):
#     print('Plant', counter, ': ',end='')
#     counter += 1
#     common = plant.find('common').text
#     botanical = plant.find('botanical').text.capitalize()
#     print(common+' ('+botanical+')')

# exercise b)
# for plant in root:
#      if plant[3].text == 'SUN':
#          print ('Plant', counter, ':', plant[0].text, '('+plant[1].text.capitalize()+')')
#          counter += 1

# exercise b) other method
for plant in root.iter('plant'):
     light = plant.find('light').text
     if light == 'SUN':
         print('Plant', counter, ': ', end='')
         counter += 1
         print(plant[0].text+' ('+plant[1].text.capitalize()+')')
