import nltk
import os
import pyperclip

def tokenizer(text):
	processed = ""
	sentences = nltk.tokenize.sent_tokenize(text)
	for sentence in sentences:
		lines = sentence.splitlines()
		for line in lines:
			if line.strip() != "":
				processed += f"{line}\n"
	return processed

text = pyperclip.paste()
processed = tokenizer(text)
path = os.path.join(os.environ['USERPROFILE'], "Desktop", "Processed.txt")
with open(path, "w", encoding="utf-8") as file:
	file.write(processed)