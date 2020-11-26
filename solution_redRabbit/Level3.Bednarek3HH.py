def run(zettel):
    dictionary = {}
    
    for words in zettel:
        dictionary[words.upper()] = dictionary.get(words.upper(),0) + 1

    sentence = "LASTCHRISTMAS"
    sum = 0
    for x in sentence:
        sum = sum + dictionary[x]
        binary = bin(sum)[2:]

    return compress(binary)
            
def compress(binaereZahl):
    finish_number = []
    anzEins = 0
    anzNull = 0
    laengeZahl = len(binaereZahl)

    for index, elem in enumerate(binaereZahl, start=0):
        if elem == "1":
            anzEins += 1
            if index+1 < laengeZahl:
                if binaereZahl[index+1] != "1":
                    finish_number.append(anzEins)
                    anzEins = 0
                else:
                    continue
            else:
                finish_number.append(anzEins)
        else:
            anzNull +=1
            if index+1 < laengeZahl:
                if binaereZahl[index+1] != "0":
                    finish_number.append(anzNull)
                    anzNull = 0
                else:
                    continue
            else:
                finish_number.append(anzNull)

    return finish_number