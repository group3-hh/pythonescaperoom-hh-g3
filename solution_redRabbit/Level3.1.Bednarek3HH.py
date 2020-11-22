def run(zettel):
    dictionary = {}
    
    for words in zettel:
        dictionary[words.upper()] = dictionary.get(words.upper(),0) + 1

    sentence = "MERRYCHRISTMAS"
    sum = 0
    for x in sentence:
        sum = sum + dictionary[x]
        binary = bin(sum)[2:]

    return compress(binary)
            
def compress(zahl):
    whole_number = 0
    first_number = "1"
    finish_number = []
   
    for element in zahl:
        if element != first_number:
            finish_number.append(whole_number)
            whole_number = 0
        whole_number += 1
        first_number = element
    finish_number.append(whole_number) 
    return finish_number
