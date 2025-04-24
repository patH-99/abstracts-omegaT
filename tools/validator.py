import xml.etree.ElementTree as ET

# Defining the XML namespace
namespaces = {
    'xml': 'http://www.w3.org/XML/1998/namespace'
}

# Parsing the TMX file
tree = ET.parse('/Users/patrikhrabanek/PycharmProjects/cooking/abstracts_1st_half_training.tmx')  # Replace with the actual path to your TMX file
root = tree.getroot()

# Iterating over the translation units and extracting the segments
for tu in root.findall(".//tu"):
    cs = tu.find(".//tuv[@xml:lang='cs']/seg", namespaces=namespaces)
    if cs is not None:
        print(cs.text)
