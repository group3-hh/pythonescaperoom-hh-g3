import random
import string
import json
import os.path
from EscapeRoom import EscapeRoom

if os.path.isfile('rezept.txt'):
    level = 2
else:
    level = 1


class Elvira(EscapeRoom):


    def __init__(self):
        super().__init__()
        self.set_metadata("Achim", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())


    def create_level1(self):
        numbers = []
        for i in range(0, 500):
            n = random.randint(70, 1300)
            numbers.append(n)
        if level == 1:
            task_messages = [
                "Mit brummenden Schädel erwachte der rot bemantelte Mann. Nie wieder den selbgepanschten Eierlikör des langorhigen schwor er sich",
                "Verdammt dunkel hier, wie war noch die Pin seines Handy? Natürlich hatte dieser pelzige Eierdieb wieder seine Pin geändert",
                "Und wie beim letztem Mal klebte ein Zettel an seinem Handy",
                f"Merke dir folgende Zahlen: <b> {numbers} </b ",
                "Suche dir die größte gerade dreistellige Zahl die kein Zahlenpalindrom ist und deren Umkehrzahl kleiner ist als sie selbst.",
                "Subtrahiere davon deren Umkehrzahl und addiere zu diesem Ergebnis wiederum die Umkehrzahl des Ergebnisses.",
                "Und zack da ist deine Pin",
                "Ach ja... ,wenn das erste Teilergebnis ein zweistelliges Ergebnis zur Folge hat, stellt man der Zahl eine Null voran.",
            ]
        else:
            task_messages = [
                "<b> On Night before </>",
                "Zugegeben der Likör war ein bisschen stärker als sonst, aber das der bärtige so schnell aus den Latschen kippt....",
                "Vielleicht besser so, jedes Jahr das selbe...einen Tag bevor er arbeiten muss.... nur gejammer",
                "Ok, noch nen lütten... aber dann ab ist Schluss ",
                "\"Hui, der is ja komplett weggetreten muahahah... Morgen muss er Arbeiten... Ich mal ihm was ins Gesicht\"",
                "\"Nein warte... das wäre kindisch.... Ich rasier ihm den Bart ab.... Nein warte ... das hatten wir schon und er wäre fast gefeuert worden",
                "\"Ok erstmal sein Handy Pin ändern\"",
                "Er wusste, dass sein Kompanion Rätsel hasste, warum sonst waren alle Sudoku im Bad unangetastet?",
                "Also würden er ein paar Rätsel testen, aber vorher noch nen lütten",
                f"Merke dir folgende Zahlen: <b> {numbers} </b ",
                "Suche dir die kleinste ungerade dreistellige Zahl die kein Zahlenpalindrom ist und deren Umkehrzahl kleiner ist als sie selbst.",
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
        liste = ['5663686e61' ,'454255a547' ,'5663666e61' , '5ac4e54e45' , '6adc4e4445','429c434b45','c45256a45','57d64c46c5','5a41484d65','4a4f1b4552','27d74c43c5' ,'5a4f464542 ','46796e6573 ','64f6727065 ','4b7c49434b ','624c49334b','666c67734b' ,'505041545a','4bd6544562','1c414e5a45','4c454e5645','ebc4534947','4b6c495050','686c696666','6b6c616d6d','5a31554e53','5a61756e73','7a61756e73']

        if level == 1:
            task_messages = [
                "\"Du hast dein Handy entsprerrt!!! Nice! 1089 Hammerzahl und mega belastend wenn man drüber nachdenkt\"" ,
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

        else:
            task_messages = [
                "\"Verdammt Peter\" Anmerkung des Erzählers: Peter hieß sein Einhorn Hüpftier \"Du hast seine seine Zugangskarte\"",
                "Würde er seine Zugangskarte nicht holen würden weder fossile Brennstoffe noch Kariusverursachende Substanzen in saubere Schuhe gestecken werden",
                "",
                "",

                ]


            hints = [
                "Sieht genaus so aus wie beim ersten Mal? Lies den Text noch mal",
                "Die Liste ist die selbe, das Erbniss auch.... als wäre das Level ein Spiegel des ersten Durchlaufen",
                "Er schrieb den Text für den Test nicht neben dem Spiegel!",
            ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level2, "data": liste}

    def create_level3(self):
        meng = ['achtSEPERATOREigelb','250 gSEPERATORPuderzucker','375 mlSEPERATORKondensmilch','8 gSEPERATORVanillezucker','250 mlSEPERATORRum']

        if level == 1:

            task_messages = [
                "Du hast es geschafft und damit du weißt, was den Nikolaus so umgehauen hat und du für Weihnachten eventuell ein Geschenk hast. Hier deine Belohnung !! ",
                "Danach ist auch wirklich Schluss! Wirklisch. Die Zutatenliste enthält durch einen dummen Zufall die Zutaten und Mengenangabe und auch noch in der falschen Reihenfolge",
                "Entferne und merke dir jedes 3 dritte Zutat aus der Liste, bis sie leer wird.",
                "Mach das selbe mit der Mengenangabe allerdings nimm hier jede 5 aus der Liste, bis sie leer wird.",
                "Füge das ganze zu einem Wörterbuch mit der Zutat und der Mengenangabe zusammen und schicke es mir ;).",
                f"<b> {meng} </b ",
                "Und ja.... das ist nur die Zutatenliste.... Spiele noch mal und die Ganze geschichte zu erfahren und das Rezept zu vervollständigen.",
                "Restarte den Webserver und betrette den Raum noch mal",
            ]



            hints = [
                "Aktuell ist es eine Liste... was es schwer macht diese zu sortieren, nicht nur Glück kann sich verdoppeln wenn man es teilt ;) ",
                "Das Wort SEPERATOR could be literally used as a ?",
                "Ein Beispiel: [1,2,3,4,5] - sortiere indem du dir jeden 3. Zeichen merkst und es dann lösche bis nichts mehr übrig ist: 3 -> [1,2,4,5], weiterzählen bei 4: 1 -> [2,4,5] ",
                "weiter mit dem Beispiel: wir haben 3,1 und übrig [2,4,5] -> weiter -> 3,1,5 [2,4] -> 3,1,5,2 [4] -> 3,1,5,2,4",

                ]
        else:

            task_messages = [
                "Nun ist es geschafft",
                "Du findest nach dem Beantworten der folgenden Frage das Rezept des legendären Eierlikörs in der Datei rezept.txt",
                "im Startordner. Viel Spaß beim nachmachen",
                "Final Question: Sollte dieser Escaperoom die volle Punktzahl erhalten ? (Ja/Nein)",
                "es gibt nur eine richtige Antwort !"
            ]

            hints = [
                "Die Antwort ist nicht Nein ;)"
            ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level3, "data": meng}

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
                    count += 1
        if level == 1:
            erg = bytes.fromhex(erg).decode('utf-8')[::-1]
        else:
            erg = bytes.fromhex(erg).decode('utf-8')
        return erg

    def level3(self,meng):

        list1 = [i.split('SEPERATOR')[0] for i in meng]
        list2 = [i.split('SEPERATOR')[1] for i in meng]
        rezp = {}
        ant = "Ja"

        def create_liste(nliste, intr):
            pos = intr - 1
            index = 0
            len_list = (len(nliste))
            temp1 = []

            for i in range(len_list):

                while len_list > 0:
                    index = (pos + index) % len_list

                    temp1.append(nliste[index])
                    nliste.pop(index)
                    len_list = (len(nliste))
            return temp1

        menge = create_liste(list1, 3)
        zutat = create_liste(list2, 5)

        rezp = {zutat[i]: menge[i] for i in range(5)}
        rezp2= 'Zuerst die Eidotter und den Vanillezucker schaumig schlagen, langsam den Puderzucker unterrühren und die' \
               ' Kondensmilch dazugeben. Nun langsam den Rum unterrühren (je nachdem wie "alkoholisch" ihr den Eierlikör ' \
               'mögt, könnt es auch ein bissel mehr sein...). Das Ganze wird nun im Wasserbad langsam erhitzt. Das geht ' \
               'am besten, wenn man einen kleineren Topf in einen größeren stellt. Dabei immer wieder umrühren. Solange ' \
               'bis es schön dickflüssig wird, aber es sollte auf keinen Fall kochen! Noch warm in Flaschen abfüllen und ' \
               'diese nicht ganz voll machen, weil der Eierlikör beim Abkühlen noch fester wird und man oftmals noch mit ' \
               'Milch oder Rum auffüllen muss, um ihn wieder aus der Flasche zu kriegen.'

        if level == 1:
                with open('rezept.txt', 'w') as file:
                    file.write(json.dumps(rezp))
                return rezp
        else:
            with open('rezept.txt', 'a') as file:
                file.write(rezp2)
            return ant


