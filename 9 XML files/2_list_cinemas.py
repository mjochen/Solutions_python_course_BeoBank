import xml.etree.ElementTree as ET

xmlDoc = ET.parse("cinemas.xml")
root = xmlDoc.getroot()

print('Cinemas in Antwerp')
# for cinema in root.findall('bioscoopoverzicht'):
#     print(cinema.find('naam').text)
#     print(cinema.find('straat').text, cinema.find('huisnummer').text)
#     print(cinema.find('postcode').text, cinema.find('district').text+'\n')

#other method
for cinema in root:
    print(cinema[4].text)
    print(cinema[5].text, cinema[6].text)
    print(cinema[7].text, cinema[8].text)
    print()