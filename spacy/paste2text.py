import os
import pyperclip
import spacy

def tokenizer(text):
    # Load tokenizer
    nlp = spacy.load("en_core_web_sm")

    # Process text
    processed = ""
    doc = nlp(text)
    sentences = doc.sents
    for sentence in sentences:
        lines = sentence.text.splitlines()
        for line in lines:
            if line.strip() != "":
                processed += f"{line}\n"

    return processed

text = pyperclip.paste()
processed = tokenizer(text)
path = os.path.join(os.environ['USERPROFILE'], "Desktop", "Processed.txt")
with open(path, "w", encoding="utf-8") as file:
    file.write(processed)