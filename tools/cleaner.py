import html

def escape_xml_special_characters(text):
    """
    This function takes a string and escapes the common special characters to make it XML-safe.
    """
    # Escape common XML special characters
    escaped_text = html.escape(text)

    # Additional replacements for specific characters used in Czech or other languages
    escaped_text = escaped_text.replace('’', '&apos;')  # Right single quotation mark
    escaped_text = escaped_text.replace('‘', '&lsquo;')  # Left single quotation mark
    escaped_text = escaped_text.replace('“', '&quot;')  # Left double quotation mark
    escaped_text = escaped_text.replace('”', '&quot;')  # Right double quotation mark
    escaped_text = escaped_text.replace('–', '&ndash;')  # En dash
    escaped_text = escaped_text.replace('—', '&mdash;')  # Em dash

    return escaped_text

# Example usage
text = "Suffixless action nouns are mostly analysed as deverbal derivatives (e.g., výběr ‘choice’ < vybírat ‘to choose.IPFV’), but dictionaries ascribe the reverse direction to some noun–verb pairs (útok ‘attack’ > útočit ‘to attack.IPFV’) despite being both formally and semantically close to the former type. The question is addressed in the present study of whether any linguistic features can be identified in pairs of suffixless nouns and directly corresponding verbs that would speak in favour of one or the other direction. The analysis of 250 Czech suffixless nouns reveals a correlation between the number of directly related verbs derived by suffixes and the direction as recorded in the dictionaries: While deverbal nouns correspond mostly to a pair of verbs with different (aspect-changing) suffixes (cf. výběr ‘choice’ : vybrat/vybírat ‘to choose.PFV/IPFV’), nouns that are bases for verbs tend to share the root with a single (imperfective) verb (útok ‘attack’ : útočit ‘to attack.IPFV’). This correlation is elaborated into two different paradigms, one being based on verbal roots while the other on nominal roots, which might be applicable in hypothesizing the direction also with nouns that are not covered by the dictionaries."


escaped_text = escape_xml_special_characters(text)
print(escaped_text)
