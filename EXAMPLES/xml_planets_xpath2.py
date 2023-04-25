
# import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('../DATA/solar.xml')

jupiter = doc.find('.//planet[@planetname="Jupiter"]')

if jupiter is not None:
    for moon in jupiter:
        print(moon.text)  # grab attribute
print('=' * 60)

for planet in doc.findall('.//planet[moon]'):
    print(planet.get('planetname'), end=' ')
print('\n')
