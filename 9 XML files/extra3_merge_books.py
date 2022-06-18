import xml.etree.ElementTree as ET

xmldoc1 = ET.parse("books1.xml")
root1 = xmldoc1.getroot()

xmldoc2 = ET.parse ("books2.xml")
root2 = xmldoc2.getroot()

for node in root2:
     root1.append(node)

xmldoc1.write('books_all.xml')