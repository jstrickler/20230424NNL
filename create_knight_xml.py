import lxml.etree as et
# import xml.etree.ElementTree as et

root = et.Element("knights")

with open('DATA/knights.txt') as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip().split(':')
        knight = et.SubElement(root, "knight", name=name)
        knight_color = et.SubElement(knight, "color")
        knight_color.text = color
        et.SubElement(knight, "quest").text = quest
        et.SubElement(knight, "comment").text = comment


print(et.tostring(root, xml_declaration=True, pretty_print=True).decode())