import json
with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

def clean_word(word):
    word = word.replace("ः", "")
    if word.endswith("ाः"):
        word = word[:-2]
    return word

sentence = input("Enter Sanskrit sentence: ")
words = sentence.split()

translated = []

for word in words:
    clean = clean_word(word)
    translated.append(dictionary.get(clean, "[unknown]"))

print("Odia Translation:", " ".join(translated))