#dictionary

baby_first_words = {
    "A": "Apple",
    "B": "Ball",
    "C": "Car"
}

print(baby_first_words["A"])

#add items to existing dictioanry

baby_first_words["D"]= "dog"

#print ALL ITEM IN DICTIONARY

for items in baby_first_words:
    print(items)
    print(baby_first_words[items])
