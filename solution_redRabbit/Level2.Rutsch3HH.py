def run(liste):
    magische_zahl_1 = potenz = 2

    loesung = []
    while len(str(magische_zahl_1)) < len(liste):
        magische_zahl_1 = 1089 ** potenz
        potenz += 1

    for i in range(len(liste)):
        x = str(magische_zahl_1)[i]
        loesung.append(liste[i][int(x)])
    loesung = ("".join(loesung))
    loesung = bytes.fromhex(loesung).decode('utf-8') [::-1]
    return loesung
