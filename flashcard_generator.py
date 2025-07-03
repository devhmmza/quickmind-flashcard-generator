import spacy

nlp = spacy.load("en_core_web_sm")

def generate_flashcards(text):
    doc = nlp(text)
    flashcards = []

    for sent in doc.sents:
        ents = list(sent.ents)
        if ents:
            ent = ents[0]  
            answer = ent.text
            
            question = sent.text.replace(answer, "_____")
            flashcards.append((question.strip(), answer.strip()))

    return flashcards
