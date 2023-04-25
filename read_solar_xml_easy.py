import lxml.etree as et

XML_FILE = "DATA/solar.xml"

doc = et.parse(XML_FILE)

for planet in doc.findall('.//planet'):  # using xpath
    print(planet.get("planetname"))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")


