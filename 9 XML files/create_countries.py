import xml.etree.ElementTree as ET
root = ET.Element('countries')
# append two nodes to the root
finland = ET.Element('country')
root.append(finland)
finland.text = 'Finland'
sweden = ET.Element('country')
sweden.text = 'Sweden'
root.append(sweden)
# append third element with different working method
ireland = ET.SubElement(root, 'country')
ireland.text = 'Ireland'

tree = ET.ElementTree(root)
tree.write('countries.xml', encoding='utf-8', xml_declaration='True')
