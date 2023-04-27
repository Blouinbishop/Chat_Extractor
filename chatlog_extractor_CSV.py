import spacy
import csv

def csv_extractor(file_path, text_column_name):
   
    # Read in the CSV file
    with open(file_path, 'r', encoding='utf-8') as f: # encoding used with twitch chat IRC make sure it matches 
        # using utf 8
        reader = csv.DictReader(f)
        # Combine all rows into one string
        chat_text = ' '.join([row[text_column_name] for row in reader])


# Using spaCy to sort the text
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(chat_text)

# Extract named entities
    entities = [(entity.text, entity.label_) for entity in doc.ents]

# creating noun and verb arrays, passing the text information into category of verb or noun
    nouns = []
    verbs = []


# loop through the document or text pulled from spaCy
    for token in doc:
    # token checks if text is noun or verb
     if token.pos_ == 'NOUN':
        nouns.append(token.text)
     elif token.pos_ == 'VERB':
        verbs.append(token.text)
        # append is adding it to the array/list 

# Prints all the named entities, nouns, and verbs
    print('Named Entities:', entities)
# print spacer statements for clarity of the output
    print('')
    print('')
    print('Nouns:', nouns)
    print('')
    print('')
    print('Verbs:', verbs)

# Just a if statement to call into terminal "main"
if __name__ == '__main__':
    file_path = 'C:/Users/bloui/Classcode/chat.csv'
    #change the arguemnt for CSV path 'message' can be changed to other categories
    csv_extractor(file_path, 'message')
