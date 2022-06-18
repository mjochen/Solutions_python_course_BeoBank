import xml.etree.ElementTree as ET
xmlDoc = ET.parse('drugs.xml')
root = xmlDoc.getroot()

for leaflet in root.findall('leaflet'):
     forms = leaflet.find('pharmaceutical_forms')
     leaflet.remove(forms)
     name = leaflet.find('name')
     name.text = name.text.upper()

xmlDoc.write('drugs_changed.xml')