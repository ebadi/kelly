import csv

file_path = "Swedish-Kelly_M3_CEFR.csv"


def short(word):
    if word == "noun-en":
        return "en"
    elif word == "noun-ett":
        return "ett"
    elif word == "adverb":
        return "adv"
    elif word == "adjective":
        return "adj"
    elif word == "verb":
        return "vb"
    else:
        return word

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        short_class = short(row["class"])
        print( f"{row["word"]} ({short_class})", end='    ')