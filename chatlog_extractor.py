import spacy
 

def chatlog_extractor(file_path):
   
    # Open the chat log file and read in its contents
    with open(file_path, 'r', encoding='utf-8') as f:
        # encoding used with twitch chat IRC make sure it matches 
        # using utf 8
        chat_text = f.read()

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
#print spacer statements for clarity of the output
    print('')
    print('')
    print('Nouns:', nouns)
    print('')
    print('')
    print('Verbs:', verbs)

# Just a if statement to call into terminal "main"
if __name__ == '__main__':
    file_path = 'C:/Users/bloui/Classcode/chat2.txt' # file type should match function call .txt
    chatlog_extractor(file_path)
