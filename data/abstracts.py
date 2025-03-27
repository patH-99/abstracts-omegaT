import json

input_file = '/Users/patrikhrabanek/Downloads/corpus.jsonl'
output_file = 'abstracts.tmx'

# Initialize the TMX file format
tmx_header = """<?xml version="1.0" encoding="UTF-8"?>
<tmx version="1.4">
  <header creationtool="Python Script" creationtoolversion="1.0" datatype="PlainText" segtype="sentence" o-tmf="XML" adminlang="en" srclang="cs"/>
  <body>
"""

tmx_footer = """
  </body>
</tmx>
"""

# Open the JSONL file and start extracting the text
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(tmx_header)

    for line in infile:
        data = json.loads(line)
        source_text = data['abstract_cs'].strip()  # Czech text
        target_text = data['abstract_en'].strip()  # English text

        # Create TMX segment entry
        tmx_entry = f"""
        <tu>
            <tuv xml:lang="cs">
                <seg>{source_text}</seg>
            </tuv>
            <tuv xml:lang="en">
                <seg>{target_text}</seg>
            </tuv>
        </tu>
        """
        outfile.write(tmx_entry)

    outfile.write(tmx_footer)

print(f"TMX file created: {output_file}")
