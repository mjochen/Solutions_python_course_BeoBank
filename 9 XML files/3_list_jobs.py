import xml.etree.ElementTree as ET
xmlDoc = ET.parse('jobs.xml')
root = xmlDoc.getroot()

print('Overview IT vacancies:\n')
counter = 0
for company in root.find('jobs'):
     name_company = company[0].text
     contact_person = company[1].find('email').text
     vacancies= company.find('vacancies')
     for vacancy in vacancies:
         position = vacancy[0]
         if position.get('group') == 'IT':
             counter += 1
             print(str(counter)+'.\t', 'Position:\t', position.text)
             print('\t', 'Company:\t', name_company)
             print('\t', 'Contact:\t', contact_person, '\n')


