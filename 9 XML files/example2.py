import xml.etree.ElementTree as ET
xmlDoc = ET.parse("customers2.xml")
root = xmlDoc.getroot()

# print('All customers:')
# for customer in root.findall('customer'):
#     name = customer[0].text
#     type = customer.get('type')
#     print(name + ' (' + type + ')')

print('All orders:')
for customer in root.iter('customer'):
    name = customer.find('name')
    print(name.text)
    for item in customer.find('orders'):
        print('\t' + item[0].text + ': ' + item[1].text)

# print('Private customers')
# for client in root.findall('private_customer'):
#     naam = client.find('name').text
#     print('\t', naam)
#
#
# print('\nCompanies')
# for client in root.findall('company'):
#     naam = client.find('name').text
#     print('\t', naam)


# tekst = 'Python'
# for letter in tekst:
#     print(letter)
#
# fruits = ['banana', 'apple', 'pear']
# for fruit in fruits:
#     print(fruit)
#
# numbers = [100, 200, 300, 400]
# for number in numbers:
#     print(number)
