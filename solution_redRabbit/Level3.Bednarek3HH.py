def run(zettel):
    dictionary = {}
    
    for words in zettel:
        dictionary[words.upper()] = dictionary.get(words.upper(),0) + 1

    sentence = "LASTCHRISTMAS"
    sum = 0
    for x in sentence:
        sum = sum + dictionary[x]
        binary = bin(sum)[2:]
    return binary