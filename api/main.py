from docx import Document


# Function to read .docx files and return a list of lines (sentences or paragraphs)
def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text.strip())
    return text


# Load the reference and candidate .docx files
reference_file = '/Users/patrikhrabanek/OmegaT_translations/EN-SR_corpus/target/recipe_1.docx'  # Path to the reference .docx file
candidate_file = '/Users/patrikhrabanek/OmegaT_translations/EN-SR_corpus/target/recipe_1_copy.docx'  # Path to the candidate .docx file

reference_text = read_docx(reference_file)
candidate_text = read_docx(candidate_file)

# Print the content to verify
print("Reference Text:", reference_text)
print("Candidate Text:", candidate_text)

import sacrebleu

# Calculate BLEU score using sacrebleu
bleu = sacrebleu.corpus_bleu(candidate_text, [reference_text])

print(f"BLEU score: {bleu.score}")
