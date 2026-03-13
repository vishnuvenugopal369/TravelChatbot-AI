import spacy
import dateparser

nlp = spacy.load("en_core_web_sm")

def parse_query(text):

    doc = nlp(text)

    origin = None
    destination = None
    date = None

    for ent in doc.ents:

        if ent.label_ == "GPE":
            if not origin:
                origin = ent.text
            else:
                destination = ent.text

        if ent.label_ == "DATE":
            date = dateparser.parse(ent.text)

    return origin, destination, date
