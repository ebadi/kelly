import csv

file_path = "Swedish-Kelly_M3_CEFR.csv"

prompt = "\n\nvälj de 30 vanligaste orden och gör en vardaglig konversation med dessa ord: "
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    counter = 0
    day = 0
    for row in reader:
        counter += 1
        if counter % 40 == 0:
            day += 1
            print( f"{row["word"]}", end='\n\n\n# day:' + str(day) + prompt)
        else:
            print( f"{row["word"]}", end=', ')