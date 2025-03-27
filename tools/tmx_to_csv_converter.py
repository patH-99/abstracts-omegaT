import xml.etree.ElementTree as ET
import csv

# Define the XML namespace
namespaces = {
    'xml': 'http://www.w3.org/XML/1998/namespace'
}

# Parse the TMX file
tree = ET.parse('/Users/patrikhrabanek/PycharmProjects/cooking/abstracts_2nd_half_test.tmx', parser=ET.XMLParser(encoding="utf-8"))
root = tree.getroot()

# Open the CSV file for writing
with open('abstracts_corpus_2nd_half_test.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['cs', 'en'])  # Column headers for Czech and English

    # Loop through each translation unit in the TMX
    for tu in root.findall(".//tu"):
        # Extract Czech and English segments using the correct namespace
        cs = tu.find(".//tuv[@xml:lang='cs']/seg", namespaces=namespaces)
        en = tu.find(".//tuv[@xml:lang='en']/seg", namespaces=namespaces)

        if cs is not None and en is not None:  # Ensure both languages are available
            writer.writerow([cs.text, en.text])

print("CSV file created.")
