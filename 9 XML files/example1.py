import xml.etree.ElementTree as ET

xmlDoc = ET.parse("customers.xml")
root = xmlDoc.getroot()
# print(root.tag, root.attrib)
#
# for child in root:
#     print(child.tag, child.attrib)
# print(root[0].tag)
# print(root[0].attrib)
# print(root[0][0].tag)
# print(root[0][0].text)
# print(root[0][1].tag)
# print(root[0][1].text)
# print(root[3][0].tag)
# print(root[3][0].text)
# print(root[3][1].tag)
# print(root[3][1].text)

print('The file contains', len(root), 'customers.')
for customer in root.iter('customer'):
    print('name:', customer[0].text)
    print('phone:', customer[1].text)
    print('discount:', customer.get('discount'))
    print('language:', customer.get('language'))