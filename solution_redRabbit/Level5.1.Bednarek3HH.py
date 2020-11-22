import csv

def run(story):
    new_text = ""
    liste = story.split(" ")
    for element in liste:
        new_text = new_text + zeige_abkuerzung(element) + " "
    return new_text

def zeige_abkuerzung(element):
    file = open("du.csv", "r")
    reader = csv.DictReader(file)
    dictionary = {}
    for row in reader:
        dictionary[row['Elements']] = row['Abkuerzung']
    if element in dictionary:
        return dictionary[element]
    else:
        return element
  