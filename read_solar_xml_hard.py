import lxml.etree as et

XML_FILE = "DATA/solar.xml"

doc = et.parse(XML_FILE)
root = doc.getroot()

print("root: {} {}".format(root, root.tag))

for node in root:
    if node.tag.endswith('planets'):
        for planet in node:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"    {moon.text}")
print()