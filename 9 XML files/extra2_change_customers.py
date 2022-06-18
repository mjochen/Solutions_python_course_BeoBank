import xml.etree.ElementTree as ET

xmlDoc = ET.parse("customers.xml")
root = xmlDoc.getroot()

for customer in root.findall('customer'):
    language_customer = customer.get('language')
    discount_customer = customer.get('discount')
    customer.attrib = {}
    name = customer.find('name')
    name.set('language', language_customer)


    discount = ET.SubElement(customer, 'discount')
    discount.text = discount_customer

xmlDoc.write('customerchanged.xml')


