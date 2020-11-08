import random
import string
from EscapeRoom import EscapeRoom


class Elvira(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Achim", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())


    def create_level1(self):
        numbers = []
        for i in range(0, 500):
            n = random.randint(70, 1300)
            numbers.append(n)
        task_messages = [
            "Mit brummenden Schädel erwachte der rot bemantelte Mann. Nie wieder den selbgepanschten Eierlikör des langorhigen schwor er sich",
            "Verdammt dunkel hier, wie war noch die Pin seines Handy? Natürlich hatte dieser pelzige Eierdieb wieder seine Pin geändert",
            "Und wie beim letztem Mal klebte ein Zettel an seinem Handy",
            f"Merke dir folgende Zahlen: <b> {numbers} </b ",
            "Suche dir die größte gerade dreistellige Zahl, deren Umkehrzahl kleiner ist als sie selbst.",
            "Subtrahiere davon deren Umkehrzahl und addiere zu diesem Ergebnis wiederum die Umkehrzahl des Ergebnisses.",
            "Und zack da ist deine Pin",
            "Ach ja... ,wenn das erste Teilergebnis ein zweistelliges Ergebnis zur Folge hat, stellt man der Zahl eine Null voran.",
        ]

        hints = [
            "Beispiel aus 321 wird die Umkehrzahl 123",
            "Aus 99 würde 099 werden",
            "321 - 123 = 198 und 198 + 891",
            "Fall sich eine 2. stellige Zahl aus der ersten Operation ergibt: 473 - 374 = 099 und 099 + 990",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level1, "data": numbers}

    def create_level2(self):
        liste = ['5663686e61','454255a547','5663666e61','5ac4e54e45','6adc4e4445','429c434b45','c45256a45','57d64c46c5','5a41484d65','4a4f1b4552','27d74c43c5','5a4f464542','46796e6573','64f6727065','4b7c49434b','624c49334b','666c67734b','505041545a','4bd6544562','1c414e5a45','4c454e5645','ebc4534947','4b6c495050','686c696666','6b6c616d6d','5a31554e53','5a61756e73','7a61756e73']

        task_messages = [
            "\"Du hast dein Handy entsprerrt!!! Nice! 1089 Hammerzahl und mega belastend wenn man drüber nachdenkt\"",
            "Belastend war das Wort, welches ihm bei seinem Vorgesetztem Santa Claus einfiel.",
            "\"Wenn du nacher deinen Mantel hier abholst, bringst mir bitte was ausm Rewe mit?\"",
            "\"Weil du so auf Rätsel stehst hab ich dir meinen Wunsch auf dein Handy gehext. Verstehste Hex Hex! Hihi!",
            "Aber ntürlich nicht auf die simple Art. Ein bestimmtes Zeichen aus jedem Feld ergibt die Lösung",
            "Welches Zeichen? Ok kleiner Tipp: Potenziere die die magische Zahl bis du genug Ziffern hast um aus jedem Feld ein Zeichen auswählen zu können.\"",
            f": <b> {liste} </b ",
            "Genau Rätsel... das war der Grund warum er diesen Job gewählt hatte... Nicht, dass er nur einmal im Jahr arbeiten musste!",
            "Die Spielzeugproduktion hatte er vor Jahren outgesourct und wurde durch Lizenzeinnahmen finanziert",
            "welche größtenteils durch einen Namenhaften Getränkehersteller hereinsprudelten.",
            "Er konnte ihn sich vorstellen wie der langohrige da kichernd in seinem Ostergras saß und neben dem Spiegel seinen Einkaufswunsch verhexte"
        ]

        hints = [
            "Er verhexte seinen Wunsch und verbinärte ihn nicht",
            "Sieht das Rätsel nicht aus wie eine Liste mit verschiedenen Values?",
            "1089**2 sind 1185921,und damit 7 Zeichen, die Liste hat aber mehr Werte ",
            "Du hat einen Wert der mit der Anzahl der Felder in der Liste über einstimmt?",
            "Wenn du das richtige Ergebnis hast, verrät dir die erste Ziffer den geuchsten Wert im ersten Feld, die 2. Ziffer der?",
            "Er schrieb den Wunsch vor dem Spiegel!",
            "Verhext nicht war? Wenn man die Werte gegen den Spiegel hält -> 353686e6160737072716c696e656",
            "return Schnapspraline"

        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level2, "data": liste}

    ### SOLUTIONS ###

    def level1(self,numbers):
        counter = 0
        numbers.sort(reverse=True)
        gerade = [x for x in numbers if x % 2 == 0]
        a = gerade[counter]
        b = str(a)[::-1]

        while a > 998 or a < 100 or a < int(b) or a == int(b):
            counter += 1
            a = gerade[counter]
            b = str(a)[::-1]

        sum = a - int(b)
        if int(sum) <= 99:
            sum = int(sum) * 10
        d = str(sum)[::-1]
        erg = sum + int(d)
        return erg

    def level2(self,liste):
        pot = 2
        count = 0
        erg = ""

        length = len(liste)
        while (len(str(1089 ** pot))) != length:
            pot += 1
            a = 1089 ** pot

        temp_list = [int(x) for x in str(a)]
        temp_length = len(temp_list)

        for i in range(length):
            for j in liste[i]:
                if count == temp_list[0]:
                    erg = erg + str(j)
                    count = 0
                    del temp_list[0]
                    break
                else:
                    count = count + 1
        erg = bytes.fromhex(erg).decode('utf-8')[::-1]
        return erg

