import xml.etree.ElementTree as ET
root = ET.Element('compilation')

with open('songs.txt', encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    record = line.split(';')
    track = ET.SubElement(root, 'track')
    c = ET.SubElement(track, 'artist')
    c.text = record[0]
    d = ET.SubElement(track, 'song')
    d.text = record[1].strip('\n')

xmlDoc = ET.ElementTree(root)
xmlDoc.write('songs.xml', encoding="utf-8",xml_declaration=True)


