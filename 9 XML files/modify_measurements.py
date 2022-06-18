import xml.etree.ElementTree as ET

xmlDoc = ET.parse("measurements.xml")
root = xmlDoc.getroot()
# example 3
# for measurement in root.findall('measurement'):
#     number = int(measurement.find('number').text)
#     if number < 20:
#         root.remove(measurement)
# xmlDoc.write('less_measurements.xml')

# example 4
# for number in root.iter('number'):
#     new_number = int(number.text) + 1
#     number.text = str(new_number)
#     number.set('adjusted', 'yes')
# xmlDoc.write('other_measurements.xml')

# example 5
measurement = ET.Element('measurement')
measurement.set('executor', 'CF')
number = ET.SubElement(measurement, 'number')
number.text = str(77)
month = ET.SubElement(measurement, 'month')
month.text = 'December'
location = ET.SubElement(measurement, 'location')
location.text = 'Block F'
root.append(measurement)
xmlDoc.write('more_measurements.xml')
