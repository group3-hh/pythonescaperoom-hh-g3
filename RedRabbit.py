import random
import string
import json
import os.path
import sqlite3
import requests
import csv
import base64
from EscapeRoom import EscapeRoom


#csv = 'RWxlbWVudHMsQWJrdWVyenVuZw0KTmV1dHJvbixuDQpIeWRyb2dlbixIDQpIZWxpdW0sSGUNCkxpdGhpdW0sTGkNCkJlcnlsbGl1bSxCZQ0KQm9yb24sQg0KQ2FyYm9uLEMNCk5pdHJvZ2VuLE4NCk94eWdlbixPDQpGbHVvcmluZSxGDQpOZW9uLE5lDQpTb2RpdW0sTmENCk1hZ25lc2l1bSxNZw0KQWx1bWludW0sQWwNClNpbGljb24sU2kNClBob3NwaG9ydXMsUA0KU3VsZnVyLFMNCkNobG9yaW5lLENsDQpBcmdvbixBcg0KUG90YXNzaXVtLEsNCkNhbGNpdW0sQ2ENClNjYW5kaXVtLFNjDQpUaXRhbml1bSxUaQ0KVmFuYWRpdW0sVg0KQ2hyb21pdW0sQ3INCk1hbmdhbmVzZSxNbg0KSXJvbixGZQ0KQ29iYWx0LENvDQpOaWNrZWwsTmkNCkNvcHBlcixDdQ0KWmluYyxabg0KR2FsbGl1bSxHYQ0KR2VybWFuaXVtLEdlDQpBcnNlbmljLEFzDQpTZWxlbml1bSxTZQ0KQnJvbWluZSxCcg0KS3J5cHRvbixLcg0KUnViaWRpdW0sUmINClN0cm9udGl1bSxTcg0KWXR0cml1bSxZDQpaaXJjb25pdW0sWnINCk5pb2JpdW0sTmINCk1vbHliZGVudW0sTW8NClRlY2huZXRpdW0sVGMNClJ1dGhlbml1bSxSdQ0KUmhvZGl1bSxSaA0KUGFsbGFkaXVtLFBkDQpTaWx2ZXIsQWcNCkNhZG1pdW0sQ2QNCkluZGl1bSxJbg0KVGluLFNuDQpBbnRpbW9ueSxTYg0KVGVsbHVyaXVtLFRlDQpJb2RpbmUsSQ0KWGVub24sWGUNCkNlc2l1bSxDcw0KQmFyaXVtLEJhDQpMYW50aGFudW0sTGENCkNlcml1bSxDZQ0KUHJhc2VvZHltaXVtLFByDQpOZW9keW1pdW0sTmQNClByb21ldGhpdW0sUG0NClNhbWFyaXVtLFNtDQpFdXJvcGl1bSxFdQ0KR2Fkb2xpbml1bSxHZA0KVGVyYml1bSxUYg0KRHlzcHJvc2l1bSxEeQ0KSG9sbWl1bSxIbw0KRXJiaXVtLEVyDQpUaHVsaXVtLFRtDQpZdHRlcmJpdW0sWWINCkx1dGV0aXVtLEx1DQpIYWZuaXVtLEhmDQpUYW50YWx1bSxUYQ0KVHVuZ3N0ZW4sVw0KUmhlbml1bSxSZQ0KT3NtaXVtLE9zDQpJcmlkaXVtLElyDQpQbGF0aW51bSxQdA0KR29sZCxBdQ0KTWVyY3VyeSxIZw0KVGhhbGxpdW0sVGwNCkxlYWQsUGINCkJpc211dGgsQmkNClBvbG9uaXVtLFBvDQpBc3RhdGluZSxBdA0KUmFkb24sUm4NCkZyYW5jaXVtLEZyDQpSYWRpdW0sUmENCkFjdGluaXVtLEFjDQpUaG9yaXVtLFRoDQpQcm90YWN0aW5pdW0sUGENClVyYW5pdW0sVQ0KTmVwdHVuaXVtLE5wDQpQbHV0b25pdW0sUHUNCkFtZXJpY2l1bSxBbQ0KQ3VyaXVtLENtDQpCZXJrZWxpdW0sQmsNCkNhbGlmb3JuaXVtLENmDQpFaW5zdGVpbml1bSxFcw0KRmVybWl1bSxGbQ0KTWVuZGVsZXZpdW0sTWQNCk5vYmVsaXVtLE5vDQpMYXdyZW5jaXVtLExyDQpSdXRoZXJmb3JkaXVtLFJmDQpEdWJuaXVtLERiDQpTZWFib3JnaXVtLFNnDQpCb2hyaXVtLEJoDQpIYXNzaXVtLEhzDQpNZWl0bmVyaXVtLE10DQpEYXJtc3RhZHRpdW0sRHMNClJvZW50Z2VuaXVtLFJnDQpDb3Blcm5pY2l1bSxDbg0KTmlob25pdW0sTmgNCkZsZXJvdml1bSxGbA0KTW9zY292aXVtLE1jDQpMaXZlcm1vcml1bSxMdg0KVGVubmVzc2luZSxUcw0KT2dhbmVzc29uLE9n'
#csv_64_decode = base64.b64decode(csv)
#csv_result = open('du.csv', 'wb')
#csv_result.write(csv_64_decode)

if os.path.isfile('rezept.txt'):
    run = 2
else:
    run = 1


class RedRabbit(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("group", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())
        self.add_level(self.create_level4())
        self.add_level(self.create_level5())
        self.add_level(self.create_level6())
        self.add_level(self.create_level7())


    def create_level1(self):
        numbers = []
        for i in range(0, 500):
            n = random.randint(70, 1300)
            numbers.append(n)
        if run == 1:
            task_messages = [
                "Mit brummenden Schädel erwachte der rot bemantelte Mann. Nie wieder den selbst gepanschten Eierlikör des langohrigen schwor er sich",
                "Was ist heute bloß für ein Tag? Ach herrje, ein Arbeitstag. Wenn mein Vorgesetzter Santa Claus das sieht, dann bekomme ich ein dickes Problem.",
                "Mal gucken, was ich heute noch besorgen soll für ihn. Er griff nach seinem Handy.",
                "Verdammt dunkel hier, wie war noch die Pin seines Handy? Natürlich hatte dieser pelzige Eierdieb wieder seine Pin geändert",
                "Und wie beim letztem Mal klebte ein Zettel an seinem Handy",
                "Merke dir folgende Zahlen:",
                f"<b> {numbers} </b ",
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
                "\"Ok erstmal seine Handy Pin ändern\"",
                "Er wusste, dass sein Kompagnon Rätsel hasste, warum sonst waren alle Sudoku im Bad unangetastet?",
                "Also würden er ein paar Rätsel testen, aber vorher noch nen lütten",
                "Merke dir folgende Zahlen:",
                f"<b> {numbers} </b ",
                "Suche dir die kleinste ungerade dreistellige Zahl die kein Zahlenpalindrom ist und deren Umkehrzahl kleiner ist als sie selbst.",
                "Subtrahiere davon deren Umkehrzahl und addiere zu diesem Ergebnis wiederum die Umkehrzahl des Ergebnisses.",
                "Und zack da ist deine Pin",
                "Ach ja... ,wenn das erste Teilergebnis ein zweistelliges Ergebnis zur Folge hat, stellt man der Zahl eine Null voran.",

            ]

        hints = [
            "Beispiel: aus 321 wird die Umkehrzahl 123",
            "Aus 99 würde 099 werden",
            "Beispielberechnung: 321 - 123 = 198 -> daraus folgt 198 + 891",
            "Falls sich eine 2. stellige Zahl aus der ersten Operation ergibt: 473 - 374 = 099 und 099 + 990",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level1, "data": numbers}

    def create_level2(self):

        if run == 1:
            liste = ['5663686e61', '454255a547', '5663666e61', '5ac4e54e45', '6adc4e4445', '429c434b45', 'c45256a45','57d64c46c5', '5a41484d65', '4a4f1b4552', '27d74c43c5', '5a4f464542 ', '46796e6573 ','64f6727065 ', '4b7c49434b ', '624c49334b', '666c67734b', '505041545a', '4bd6544562', '1c414e5a45','4c454e5645', 'ebc4534947', '4b6c495050', '686c696666', '6b6c616d6d', '5a31554e53', '5a61756e73','7a61756e73']

            task_messages = [
                "\"Du hast dein Handy entsperrt!!! Nice! 1089 magische Zahl und mega belastend wenn man drüber nachdenkt\"" ,
                "Belastend war das Wort, welches ihm bei seinem Vorgesetztem Santa Claus einfiel.",
                "\"Wenn du nachher deine Schicht beendet hast und deinen Mantel abholst, dann bring mir bitte was aus dem Rewe Raum mit?\"",
                "\"Weil du so auf Rätsel stehst hab ich dir meinen Wunsch auf dein Handy gehext.!",
                "Aber natürlich nicht auf die simple Art. Bilde die Potenz von 1089 bis das Ergebnis genügend Ziffern hat um aus jeden Feld ein Zeichen auszuscheiden.",
                "Nutze die Ziffern um die richtigen Zeichen in den Feldern zu finde und dann füge die Zeichen zusammen bevor du sie entzauberst",
                f"<b> {liste} </b ",
                "Genau Rätsel... das war der Grund warum er diesen Job gewählt hatte... Nicht, dass er nur einmal im Jahr arbeiten musste!",
                "Die Spielzeugproduktion hatte er vor Jahren outgesourct und wurde durch Lizenzeinnahmen finanziert",
                "welche größtenteils durch einen Namenhaften Getränkehersteller hereinsprudelten.",
                "Er konnte ihn sich vorstellen wie der langohrige da kichernd in seinem Ostergras saß und neben dem Spiegel seinen Einkaufswunsch verhexte"
                ]

            hints = [
                "1089**2 sind 1185921,und damit 7 Zeichen, die Liste hat aber mehr Werte ",
                "Wenn du das richtige Ergebnis hast, verrät dir die erste Ziffer den gesuchten Wert im ersten Feld, die 2. Ziffer der?",
                "Do we count from 0 or from 1 ?",
                "Er verhexte seinen Wunsch und verbinärte ihn nicht",
                "Er schrieb den Wunsch vor dem Spiegel bevor er ihn verhexte!",
                "Verhext nicht war? Wenn man die Werte gegen den Spiegel hält -> 353686e6160737072716c696e656",
                "Die Reihenfolge ist entscheidend. Hexwert zusammenbauen, in String umwandeln, spiegeln",
                "return Schnapspraline"

            ]

        else:
            liste = ['5653686e61', '434255a547', '5663666e61', '5ac4354e45', '6adc4e4445', '428c434b45', 'c45256a45','57d64c46e5', '5a41484d65', '4a4f1b4552', '27d74c43c5', '5a4f464540', '46796e6573', '64f6720365','4b7c49434b', '624c49034b', '666c6774b', '626c67734b', '505041546a', '1bd6544562', '4c454e5645','cbc4534947', '4b6c495050', '696c696666', '6b6c616d6d', '5ae1554e53', '6a61756e73', '7a61756e75']
            task_messages = [
                "Jetzt muss ich nur noch dafür sorgen, dass er morgen beim Rewe vorbeischaut. Ich schicke ihm eine Nachricht im Namen seines Chefs, dass sollte reichen.",
                "Er sollte aber wach sein und nicht mehr im Halbschlaf.... Ich lasse ihn ein wenig rätseln, das macht wach.",
                "Nach wenigen min war das Rätsel fertig und der letzte Test ob das ganze funktionierte stand an.",
                f"<b> {liste} </b ",
                "Bilde die Potenz von 1089 bis das Ergebnis genügend Ziffern hat um aus jeden Feld ein Zeichen auszuscheiden.",
                "Dann muss nur noch der Reihenfolge nach die Zeichen ausschneiden, zusammensetzen. Sehr gut. Letzter Test und dann ab mit der Nachricht."
                ]

            hints = [
                "Sieht genaus so aus wie beim ersten Mal? Lies den Text noch mal",
                "Die Liste ist die selbe, das Erbniss auch.... als wäre das Level ein Spiegel des ersten Durchlaufen",
                "Er schrieb den Text für den Test nicht neben dem Spiegel!",
            ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level2, "data": liste}

    def create_level3(self):
        if run == 1:

            zettel = "Last Christmas, I gave you my heart but the very next day you gave it away . \
                    This year, to save me from tears I'll give it to someone special. Last Christmas, I gave you my heart but the very next day you gave it away. This year, to save me from tears I'll give it to someone special . \
                    Once bitten and twice shy I keep my distance but you still catch my eye tell me, baby do you recognize me? \
                    Well, it's been a year It doesn't surprise me ( Merry Christmas ! )  \
                    I wrapped it up and sent it with a note saying, I love you, I meant it now, I know what a fool I've been but if you kissed me now I know you'd fool me again \
                    Last Christmas, I gave you my heart But the very next day you gave it away This year, to save me from tears I'll give it to someone special"

            task_messages = [
                " Im Rewe angekommen wird es nicht besser. Lautstark dröhnt das Lied, welches keiner mehr hören kann, aus der Musikanlage.",
                " Die Musik ist so laut, dass dein Kopf förmlich platzt. Und das schlimmste: der Ohrwurm ist garantiert. Daher begibst du dich ",
                " sofort auf die Suche nach der Musikanlage, welche du hinter der Tiefkühltheke findest. Je näher du kommst, desto lauter dröhnt die Musik. ",
                " Aufhören , schreist du die Musikanlage an, jedoch passiert nichts. Hätte ich bloß nicht so viel getrunken mit dem Langohrhasen, ",
                " dann hätte ich auch sofort eine Idee gehabt, das Gerät auszustellen. Doch dann siehst du die Erlösung: um die Musik auszuschalten ",
                " musst du lediglich einen Pin von 3 Zahlen eingeben. Easy denkst du. Doch wie kriegst du den Pin heraus? ",
                " Auf einem Zettel steht:<br><br><b>" + zettel + "<br><br>"

                                                                 "<br>Gesamt: LASTCHRISTMAS",
                " Binärzahl",
                " Binärzahl komprimieren",
                " Alles klar, dann mal los!"
            ]
            hints = [
                "Zähle nach, wie oft welcher Buchstabe in dem Text, der auf dem Zettel steht, vorkommt",
                "Der Text beginnt mit Last und endet mit special",
                "Rechne die Anzahl der Zahlen, die sich hinter jedem einzelnen Buchstaben in diesem Satz Last Christmas I'll give you my heart zusammen",
                "Nun berechne aus der Dezimalzahl eine Binärzahl",
                "Dir fällt auf, dass der Pin aus 3 Zahlen besteht, die Binärzahl jedoch aus 9 Zahlen ",
                "Komprimiere daher die Binärzahl ",
                "Wichtig: Beginne vorne mit der 1 zu zählen ",
                "Gib den dreistelligen Pin ein"
            ]
        else:
            zettel = "Last Christmas, I gave you my heart but the very next day you gave it away . \
                    This year, to save me from tears I'll give it to someone special. Last Christmas, I gave you my heart but the very next day you gave it away. This year, to save me from tears I'll give it to someone special . \
                    Once bitten and twice shy I keep my distance but you still catch my eye tell me, baby do you recognize me? \
                    Well, it's been a year It doesn't surprise me ( Merry Christmas ! )  \
                    I wrapped it up and sent it with a note saying, I love you, I meant it now, I know what a fool I've been but if you kissed me now I know you'd fool me again \
                    Last Christmas, I gave you my heart But the very next day you gave it away This year, to save me from tears I'll give it to someone special "

            task_messages = [
                "Wie gut das heute alles in der Cloud läuf."
                "Als er letztes Jahr auf seiner Tour war, fand er den Zettel mit den Zugangsdaten."
                "Und seit dem Tag konnte er mit seinem Spotifyaccount mit sämtlichen Rewemärkten verknüpfen."
                "Und er hatte eine Playlist speziell für diesen Tag. 24/7 never ending: "
                "Die Zugangsdaten sind nur ein Pin von 3 Zahlen."
                "Auf dem Zettel steht:<br><br><b>" + zettel + "<br><br>"
                                                              "<br>Gesamt: MERRYCHRISTMAS",
                " Binärzahl",
                " Binärzahl komprimieren",
                " Alles klar, dann mal los!"

            ]
            hints = [
                "Zähle nach, wie oft welcher Buchstabe in dem Text, der auf dem Zettel steht, vorkommt",
                "Der Text beginnt mit Last und endet mit special",
                "Rechne die Anzahl der Zahlen, die sich hinter jedem einzelnen Buchstaben in diesem Satz MERRYCHRISTMAS zusammen",
                "Nun berechne aus der Dezimalzahl eine Binärzahl",
                "Dir fällt auf, dass der Pin aus 3 Zahlen besteht, die Binärzahl jedoch aus 9 Zahlen ",
                "Komprimiere daher die Binärzahl ",
                "Wichtig: Beginne vorne mit der 1 zu zählen ",
                "Gib den dreistelligen Pin ein"

            ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level3, "data": zettel}

    def create_level4(self):
        if run == 1:
            json_choice = random.choice(["{\"identitycard\":[{\"idnumber\":\"L2200AVWO2\",\"birthdate\":\"9504095\",\"expirydate\":\"2210012D\",\"totalchecknumber\":\"2\"}]}",
                                        "{\"identitycard\":[{\"idnumber\":\"N4OBZNGAA4\",\"birthdate\":\"8601012\",\"expirydate\":\"2809078D\",\"totalchecknumber\":\"4\"}]}"])
            task_messages = [
                "Der Pin lautet 0 3 5 1. Das war einfach. Endlich ist die Musikanlage still. Du hörst ein Aufschrei hinter dir: \"Hey, was machen Sie denn da? Das ist kein Spielzeug.\"",
                "Das sind die Worte, die dich aufhorchen lassen, damit du schleunigst das Weite suchst. Jetzt schnell die Schnapspraline holen und ab an die Kasse damit.",
                "Gleich geschafft, denkst du dir. Doch Moment.<br><br>",
                "Die Dame an der Kasse scannt die Schnapspraline, es ertönt ein „piep“, sie schaut die Schnapspraline an und sagt: \"Junger Herr, ehm, so wie ich das seh ist da Alkohol drin.",
                "Alkohol darf ich Ihnen nur verkaufen, wenn Sie mir beweisen, dass Sie bereits das 18. Lebensjahr vollendet haben. Ansonsten bleibt diese Schnapspraline hier bei mir!\"<br><br>",
                "Lächerlich denkst du dir, die macht es dir aber schwer. Vermutlich will die alte Dame nur an meinen Namen und meine Adresse heran, aber was soll’s.",
                "Du greifst nach deinem Personalausweis und reichst ihr diesen. Ihre Brillengläser sind dick wie ein Aschenbecher. Sie verzieht die Nase und schaut sich",
                "die maschinenlesbare Zone <b>"+json_choice+"</b> des",
                "Personalausweises ganz genau an.<br><br>",
                "\"Junger Herr, ich kann zwar sehen, dass Sie das 18. Lebensjahr vollendet haben. Jedoch ist der Personalausweis ganz klar eine Fälschung. Ziemlich frech von Ihnen.\" \"Unmöglich\",",
                "erklärst du ihr \"mein Personalausweis ist keine Fälschung.\" Die kecke Dame ergänzt: \"Dann beweisen Sie mir, dass dieser echt ist. Wenn Sie dies zeigen, dann bekommen Sie Ihre",
                "Schnapspraline und können den Laden verlassen.\"<br><br>",
                "Dann beweise es der Dame, das es sich bei der maschinenlesbaren Zone um gültige Feldinhalte handelt!"
            ]
            hints = [
                "Bei dem Element \"idnumber\" handelt es sich um die Ausweisnummer plus eine Prüfziffer, \
                bei dem Element \"birthdate\" um das Geburtsdatum im Format JJMMTT plus eine Prüfziffer, \
                bei dem Element \"expirydate\" um das Ablaufdatum des Ausweises im Format JJMMTT plus eine Prüfziffer gefolgt von einem Länderkennzeichen und \
                bei dem Element \"totalchecknumber\" um eine Prüfziffer über die zuvor genannten drei Elemente (außer dem Länderkennzeichen)!",
                "Für alle Daten wird der gleiche Algorithmus verwendet. Jede Ziffer wird links beginnend, alternierend mit 7, 3, 1 multipliziert und addiert, \
                und dann Modulo 10 genommen. Für die Gesamtprüfziffer werden alle drei Daten (inklusive der Prüfziffer, aber ohne Länderkennzeichen) \
                aneinandergehängt und ebenfalls der Algorithmus angewandt.",
                "Buchstaben müssen umgewandelt werden! A = 10, B = 11, ..."
            ]
        else:
            json_choice = random.choice(["{\"identitycard\":[{\"idnumber\":\"L9VXUWTCA7\",\"birthdate\":\"7611072\",\"expirydate\":\"2408035D\",\"totalchecknumber\":\"2\"}]}",
                                        "{\"identitycard\":[{\"idnumber\":\"T6VXYQYZU5\",\"birthdate\":\"9107038\",\"expirydate\":\"2104212D\",\"totalchecknumber\":\"9\"}]}"])
            task_messages = [
                "Bester Tag ever. Er konnte sich den verkaterten Zottel bildlich vorstellen. Frau Speckmann hatte er gebrieft,<br>",
                "sie würde ihn ein wenig aufhalten, während er prüft ob seine Playlist noch läuft.<br>",
                "Bei Frau Speckmann kaufte er häufig für sein Leibgericht ein, falscher Hase. Sie hatten sich ein paar mal auf<br>",
                "einen Kaffee getroffen und dabei hatte Sie ihm gezeigt wie man schlecht gefälschte Ausweise in der maschinenlesbaren Zone erkennt.<br><br>",
                "Wie ging dass doch gleich bei nachfolgendem Ausweis?<br><br><b>"+json_choice+"</b>"
            ]
            hints = [
                "Der Algorithmus sowie die Bedeutung der Feldinhalte der maschinenlesbaren Zone sollten dir noch aus dem vorherigen Durchlauf des Escape Rooms bekannt sein :)",
            ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level4_check_identity_card_validity, "data": json_choice}

    def create_level5(self):
        if run == 1:

            story = " Holmium Holmium Holmium and a Holmium Copper Sulfur Polonium Copper Sulfur . <br>Welcome in Americium Erbium Iodine Calcium . \
                    <br>We are in the Potassium Iodine Technetium Helium Neutron . <br>Thank you for the Scandium Hydrogen Sodium Phosphorus Sulfur Praseodymium Aluminum Iodine Neon . \
                    <br>Iodine Americium the E Arsenic Tellurium Rubidium Uranium Nitrogen Nitrogen Yttrium and Iodine Americium sitting on my Uranium Nickel Cobalt Radon and watching you . \
                    <br>On the table there are Barium Cobalt Neutron , Cobalt Oxygen Potassium Iodine Einsteinium , \
                    Fluorine Rhenium Nitrogen Carbon Hydrogen Francium Iodine Einsteinium , Barium Sodium Sodium Sulfur , \
                    <br>Carbon Holmium Cobalt Lanthanum Tellurium , Beryllium Erbium and Tungsten Iodine Neon . \
                    <br>But Iodine Americium Nobelium Neutron Aluminum Cobalt Holmium Lithium Carbon . \
                    <br>You have the Americium Boron Iodine Titanium Oxygen Nitrogen and the Polonium Tungsten Erbium to solve this riddle , \
                    because you are a good Phosphorus Lanthanum Yttrium Erbium . \
                    <br>Tungsten Oxygen Tungsten you made it this far . \
                    <br>You are very Nickel Cerium and such a Germanium Nickel Uranium Sulfur and I still want to dr Iodine Neutron Potassium with you . \
                    <br>Thorium Iodine Sulfur is your chance to get away : <br>the Phosphorus Iodine Nitrogen has three let Tellurium r Sulfur . \
                    <br>A Hydrogen Iodine Nitrogen t : It is a Phosphorus Aluminum Indium dr Oxygen me . \
                    <br>The Phosphorus Iodine Nitrogen  is  Tungsten Oxygen Tungsten \
                    <br>because it is a Phosphorus Aluminum Indium dr Oxygen me ! \
                    <br>Cobalt Nitrogen G Radium T Uranium Lanthanum Titanium Oxygen Nitrogen Sulfur ! \
                    <br>The d Oxygen Oxygen r is Oxygen Phosphorus e Nitrogen ! "

            task_messages = [
                " Du läufst aus dem Rewe heraus und verdammt, schon wieder ein verschlossener Raum. Wie gewonnen so zerronnen. ",
                " Wann endet dieses Martyrium? Du schaust dich um und erkennst, dass du in einer Küche stehst. ",
                " Es ist ziemlich benebelt im Raum und du erkennst am Ende der Küche einen finsteren Reiter.",
                " Der Reiter gibt dir einen Brief, den du entziffern musst. Auf dem Brief steht: <br><br><b>" + story + "<br><br>",
                "<br>Sobald du den Brief entzifferst und das Lösungswort vorliest, öffnet sich die Tür. "
            ]

            hints = [
                "Kommen dir bestimmte Begriffe nicht aus dem Schulunterricht bekannt vor? ",
                "Es klingt wie Harry Potter, aber es hat nichts mit ihm zutun ",
                "Es gab ein Fach in der Schule, welches sich auf die oberen Elemente bezogen haben, "
                "Richtig, der Chemie-Unterricht ",
                "Du erkennst hier Abkürzungen für die Elemente, in englischer Sprache ",
                "Rein zufällig existiert auf Github eine CSV-Datei, die Elements.csv heißt ",
                "Lies die csv-Datei ein ",
                "Versuche die Elemente durch die Abkuerzungen zu ersetzen ",
                "Anschließend kannst du den Text entschluesseln, sobald du die Abkuerzungen ersetzt hast",
                "Sobald du erkennst, wie der Pin sich zusammensetzt, musst du diesen auch noch beweisen ",
                "Dann mal los"

            ]
        else:
            story = " Holmium Holmium Holmium and a Holmium Copper Sulfur Polonium Copper Sulfur . <br>Welcome in Americium Erbium Iodine Calcium . \
                    <br>We are in the Potassium Iodine Technetium Helium Neutron . <br>Thank you for the Scandium Hydrogen Sodium Phosphorus Sulfur Praseodymium Aluminum Iodine Neon . \
                    <br>Iodine Americium the E Arsenic Tellurium Rubidium Uranium Nitrogen Nitrogen Yttrium and Iodine Americium sitting on my Uranium Nickel Cobalt Radon and watching you . \
                    <br>On the table there are Barium Cobalt Neutron , Cobalt Oxygen Potassium Iodine Einsteinium , \
                    Fluorine Rhenium Nitrogen Carbon Hydrogen Francium Iodine Einsteinium , Barium Sodium Sodium Sulfur , \
                    <br>Carbon Holmium Cobalt Lanthanum Tellurium , Beryllium Erbium and Tungsten Iodine Neon . \
                    <br>But Iodine Americium Nobelium Neutron Aluminum Cobalt Holmium Lithium Carbon . \
                    <br>You have the Americium Boron Iodine Titanium Oxygen Nitrogen and the Polonium Tungsten Erbium to solve this riddle , \
                    because you are a good Phosphorus Lanthanum Yttrium Erbium . \
                    <br>Oxygen Hydrogen Oxygen you made it this far . \
                    <br>You are very Nickel Cerium and such a Germanium Nickel Uranium Sulfur and I still want to dr Iodine Neutron Potassium with you . \
                    <br>Thorium Iodine Sulfur is your chance to get away : <br>the Phosphorus Iodine Nitrogen has three let Tellurium r Sulfur . \
                    <br>A Hydrogen Iodine Nitrogen t : It is a Phosphorus Aluminum Indium dr Oxygen me . \
                    <br>The Phosphorus Iodine Nitrogen  is  Oxygen Hydrogen Oxygen \
                    <br>because it is a Phosphorus Aluminum Indium dr Oxygen me ! \
                    <br>Cobalt Nitrogen G Radium T Uranium Lanthanum Titanium Oxygen Nitrogen Sulfur ! \
                    <br>The d Oxygen Oxygen r is Oxygen Phosphorus e Nitrogen ! "

            task_messages = [
                "Das war Frau Speckmann am Telefon.",
                "Der Schnapspralinenkurier ist auf dem Weg.",
                "Ok, Zeit für das große Finale. ",
                "Nebelmaschiene ? Check.",
                "Einhorn ? Check.",
                "Stimmenmodulator? Check.",
                "Wenn es läuft wie immer würde er, bevor er seinem Chef unter die Augen tritt, kurz in der Mitarbeiterküche halt machen",

                "Gerade noch Zeit für eine letzte Generalprobe."
            ]

            hints = [
                "Kommen dir bestimmte Begriffe nicht aus dem Schulunterricht bekannt vor? ",
                "Es klingt wie Harry Potter, aber es hat nichts mit ihm zutun ",
                "Es gab ein Fach in der Schule, welches sich auf die oberen Elemente bezogen haben, "
                "Richtig, der Chemie-Unterricht ",
                "Du erkennst hier Abkürzungen für die Elemente, in englischer Sprache ",
                "Rein zufällig existiert auf Github eine CSV-Datei, die Elements.csv heißt ",
                "Lies die csv-Datei ein ",
                "Versuche die Elemente durch die Abkuerzungen zu ersetzen ",
                "Anschließend kannst du den Text entschluesseln, sobald du die Abkuerzungen ersetzt hast",
                "Sobald du erkennst, wie der Pin sich zusammensetzt, musst du diesen auch noch beweisen ",
                "Dann mal los"
            ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level5_translate,
                "data": story}

    def create_level6(self):
        if run == 1:
            name_choice = random.choice(["Susanne",
                                        "Susanne"])
            task_messages = [
                "WOW, eine tolle Arbeit. Endlich bist du am Ziel, als du die Küche verlässt. Du entdeckst deinen roten Mantel und dein Vorgesetzter Santa Claus steht vor dir.",
                "Er verlangt die Schnapspraline, die du dem Langohrhasen noch schnell entwenden konntest, als du die Küche verlassen hast. \"Danke!\", sagt Santa Claus und fügt hinzu: ",
                "\"Endlich hast du dir deinen Feierabend verdient. Du bist für heute Abend entlassen.<br><br>",
                "Ein kleiner Rat für dich: Das nächste Mal, solltest du nicht so viel mit dem Langohrhasen bechern. Wir sehen uns dann nächstes Jahr wieder.\"",
                "Santa Claus geht zum Kamin und huscht durch diesen hindurch ins Freie.<br><br>",
                "Du durchsuchst den Raum nach der letzten Tür, da du endlich Heim möchtest, um deinen Kater auszuschlafen. Durch den Kamin passt du nicht, da du dir ordentlich",
                "Winterspeck angefuttert hast über die Adventszeit. Allmählich schaust du wie eine Seekuh aus, aber ab morgen nimmst du dir vor, eine Diät zu machen.",
                "\"Ah da ist der Ausgang!\" jubelst du fröhlich herum, als du die Tür entdeckst und zu dieser hin spurtest.",
                "\"Verdammt, schon wieder verschlossen.\", murmelst du zu dir und entdeckst einen Brief von Santa Claus. Auf diesem steht:<br><br>",
                "\"Diese Tür ist verschlossenen und alarmgesichert. Zum Öffnen dieser Tür wird eine Sicherheitskarte benötigt.\"<br><br>",
                "Nun durchsuchst du deine Tasche und findest jedoch keine Sicherheitskarte, weil du keine besitzt. Daher schaust du dir die Schnittstelle des Zutrittssystems genau an und erkennst",
                "einige wichtige Eigenschaften, da du im Programmierkurs II das Script ordentlich studiert hast. Jetzt wird es Zeit, die gelernten Tricks auch anzuwenden.<br><br>",
                "Du erkennst, dass du die Authentifizierungsmöglichkeiten dem System auch als JSON-Objekt übergeben kannst. Du weißt, dass eine <b>" + name_choice+ "</b> die Berechtigung hat, diese Tür zu öffnen.",
                "Letztendlich hat sie dir auch einmal erklärt, dass das Zutrittssystem Sicherheitslücken aufweist.<br><br>",
                "Dir gelingt es, die SQLight-Datenbank zu kopieren, die dir unter <b> https://pythonescaperoom.soeren-steinberg.de/alert.db </b> zur Verfügung steht.",
                "Du versuchst dich als Susanne auszugeben, um damit die Tür zu öffnen.<br><br>",
                "Gelingt es dir?"
            ]
            hints = [
                "Die SQLight Datenbank hat zwei Tabellen mit den Namen securitycard_owner und securitycard",
                "Die Schnittstelle des Zutrittsystems erwartet ein JSON-Objekt mit den Eigenschaftsnamen firstname, lastname, securitycard_number und pin!"
            ]
        else:
            name_choice = "Susanne"

            task_messages = [
                "Es dauerte eine geschlagene Stunde bis er sich wieder beruhigt hatte. Sein Bauch schmerzte noch immer vom vielen Lachen. Der Gesichtsausdruck .... göttlich.<br>",
                "Damit sollten doch die Grenze für 1 Mio. Abonnenten auf Youtube zu knacken sein. Aber vorher musste erstmal die geliehene Nebelmaschine und das andere Geraffel<br>",
                "wieder zurückgebracht werden, ehe jemand Fragen stellt. Die Fortbildung die Sie aus gewerkschaftlichen Gründen machen mussten hatten doch auch ihr Gutes.<br><br>",
                "Im letzten Jahr hatte ich zusammen mit dem Winterarbeiter diesen Programmierkurs gemacht. Und was trainiert besser als das Wissen in der Praxis anzuwenden.<br>",
                "War ja nicht seine Schuld dass die Lagerhalle nebenan die Zugangsdaten offen im Internet unter <b>https://pythonescaperoom.soeren-steinberg.de/alert.db </b><br>",
                "stehen ließ. Mal schauen wer ihm heute den Zutritt gewährte. Anschließend musste er zwingend telefonieren und die Wogen glätten. Kartoffelsalat und Würstchen<br>",
                "waren quasi schon vorbereitet."
            ]
            hints = [
                "Könnte es die "+name_choice+" sein, die Zugang zur Lagerhalle hat?",
                "Denk daran, der Schnittstelle des Zutrittssystems die Daten wieder als JSON-Objekt mit den Eigenschaftsnamen "
                "firstname, lastname, securitycard_number und pin zu übergeben"
            ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level6_crack_authorization, "data": name_choice}

    def create_level7(self):
        meng = ['achtSEPERATOREigelb','250 gSEPERATORPuderzucker','375 mlSEPERATORKondensmilch','8 gSEPERATORVanillezucker','250 mlSEPERATORRum']

        if run == 1:

            task_messages = [
                "Du hast es geschafft und damit du weißt, was den Nikolaus so umgehauen hat und du für Weihnachten eventuell ein Geschenk hast. Hier deine Belohnung !! ",
                "Danach ist auch wirklich Schluss! Wirklich. Die Zutatenliste enthält durch einen dummen Zufall die Zutaten und Mengenangabe und auch noch in der falschen Reihenfolge",
                "Entferne und merke dir jedes 3 dritte Zutat aus der Liste, bis sie leer wird.",
                "Mach dasselbe mit der Mengenangabe allerdings nimm hier jede 5 aus der Liste, bis sie leer wird.",
                "Füge das Ganze zu einem Wörterbuch mit der Zutat und der Mengenangabe zusammen und schicke es mir ;).",
                f"<b> {meng} </b ",
                "Und ja.... das ist nur die Zutatenliste.... Spiele noch mal und die ganze Geschichte zu erfahren und das Rezept zu vervollständigen.",
                "Restarte den Webserver und betrete den Raum noch mal",
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
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level7, "data": meng}

    ### SOLUTIONS ###

    def level1(self, numbers):
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

    def level2(self, liste):
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
        if run == 1:
            erg = bytes.fromhex(erg).decode('utf-8')[::-1]
        else:
            erg = bytes.fromhex(erg).decode('utf-8')
        return erg

    def level3(self, zettel):
        dictionary = {}

        for words in zettel:
            dictionary[words.upper()] = dictionary.get(words.upper(), 0) + 1

        if run == 1:
            sentence = "LASTCHRISTMAS"
        else:
            sentence = "MERRYCHRISTMAS"

        sum = 0
        for x in sentence:
            sum = sum + dictionary[x]
            binary = bin(sum)[2:]

        return self.compress(binary)

    def compress(self, zahl):
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

    def level4_check_identity_card_validity(self, json_choice):
        json_deserialization = json.loads(json_choice)
        id_number = json_deserialization["identitycard"][0]["idnumber"]
        birth_date = json_deserialization["identitycard"][0]["birthdate"]
        expiry_date = json_deserialization["identitycard"][0]["expirydate"]
        total_check_number = json_deserialization["identitycard"][0]["totalchecknumber"]

        id_number_is_valid = self.level4_calculate_checksum(id_number[:-1]) == int(id_number[-1])
        birth_date_is_valid = self.level4_calculate_checksum(birth_date[:-1]) == int(birth_date[-1])
        expiry_date_is_valid = self.level4_calculate_checksum(expiry_date[:-2]) == int(expiry_date[-2])

        cipher = str(id_number) + str(birth_date) + str(expiry_date[:-1])
        total_check_is_valid = self.level4_calculate_checksum(cipher) == int(total_check_number)

        if id_number_is_valid == True and birth_date_is_valid == True and expiry_date_is_valid == True and total_check_is_valid == True:
            return True
        else:
            return False

    def level4_calculate_checksum(self, cipher):
        try:
            letter_conversion = {
                '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
                'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15', 'G': '16', 'H': '17', 'I': '18',
                'J': '19', 'K': '20', 'L': '21', 'M': '22', 'N': '23', 'O': '24', 'P': '25', 'Q': '26', 'R': '27',
                'S': '28', 'T': '29', 'U': '30', 'V': '31', 'W': '32', 'X': '33', 'Y': '34', 'Z': '35'
            }

            position = 1
            sum = 0
            multiply7 = [x for x in range(1, 40, 3)]
            multiply3 = [x for x in range(2, 40, 3)]
            multiply1 = [x for x in range(3, 40, 3)]

            for character in cipher:
                if multiply7.count(position) > 0:
                    sum = sum + int(letter_conversion[character]) * 7
                if multiply3.count(position) > 0:
                    sum = sum + int(letter_conversion[character]) * 3
                if multiply1.count(position) > 0:
                    sum = sum + int(letter_conversion[character]) * 1
                position = position + 1

            return sum % 10

        except:
            return "Error calculating checksum!"

    def level5_translate(self,story):
        new_text = ""

        if run ==1:
            liste = story.split(" ")
        else:
            liste = story.split(" ")

        #liste = story.split(" ")
        for element in liste:
            new_text = new_text + self.zeige_abkuerzung(element) + " "
        return new_text

    def zeige_abkuerzung(self, element):
        file = open("du.csv", "r")
        reader = csv.DictReader(file)
        dictionary = {}
        for row in reader:
            dictionary[row['Elements']] = row['Abkuerzung']
        if element in dictionary:
            return dictionary[element]
        else:
            return element

    def level6_crack_authorization(self, name_choice):
        if self.level6_load_database_from_web(
                "https://pythonescaperoom.soeren-steinberg.de/alert.db") == True and os.path.exists(
                "alert.db") and os.access("alert.db", os.R_OK):

            db = sqlite3.connect("alert.db")
            cursor = db.cursor()
            cursor.execute(
                "SELECT firstname, lastname, securitycard_number, pin, active, date_of_expiry FROM securitycard_owner INNER JOIN securitycard on securitycard.sc_id = securitycard_owner.sc_id WHERE firstname = ? and active = 1 and date_of_expiry >= datetime('now')",
                (name_choice,))
            resultset = cursor.fetchall()
            db.close()

            if resultset:
                json_list = []
                for result in resultset:
                    json_dic = {}
                    json_dic['firstname'] = result[0]
                    json_dic['lastname'] = result[1]
                    json_dic['securitycard_number'] = result[2]
                    json_dic['pin'] = result[3]
                    json_list.append(json_dic)
                return json.dumps(json_list[0])
        else:
            print("Error - Failed to open database!")

    def level6_load_database_from_web(self, url):
        try:
            rq = requests.get(url)
            if rq.status_code == 200:
                open('alert.db', 'wb').write(rq.content)
                return True
            else:
                return False
        except:
            print("Error - No connection!")

    def level7(self,meng):

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
        rezp2 = 'Zuerst die Eidotter und den Vanillezucker schaumig schlagen, langsam den Puderzucker unterrühren und die' \
               ' Kondensmilch dazugeben. Nun langsam den Rum unterrühren (je nachdem wie "alkoholisch" ihr den Eierlikör ' \
               'mögt, könnt es auch ein bissel mehr sein...). Das Ganze wird nun im Wasserbad langsam erhitzt. Das geht ' \
               'am besten, wenn man einen kleineren Topf in einen größeren stellt. Dabei immer wieder umrühren. Solange ' \
               'bis es schön dickflüssig wird, aber es sollte auf keinen Fall kochen! Noch warm in Flaschen abfüllen und ' \
               'diese nicht ganz voll machen, weil der Eierlikör beim Abkühlen noch fester wird und man oftmals noch mit ' \
               'Milch oder Rum auffüllen muss, um ihn wieder aus der Flasche zu kriegen.'

        if run == 1:
                with open('rezept.txt', 'w') as file:
                    file.write(json.dumps(rezp))
                return rezp
        else:
            with open('rezept.txt', 'a') as file:
                file.write(rezp2)
            return ant