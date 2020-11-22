import random
import string
import csv
from EscapeRoom import EscapeRoom

class Rewe_Fertig(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Konsu", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level3(self):
        
        zettel = "Last Christmas, I gave you my heart but the very next day you gave it away . \
                This year, to save me from tears I'll give it to someone special. Last Christmas, I gave you my heart but the very next day you gave it away. This year, to save me from tears I'll give it to someone special . \
                Once bitten and twice shy I keep my distance but you still catch my eye tell me, baby do you recognize me? \
                Well, it's been a year It doesn't surprise me ( Merry Christmas ! )  \
                I wrapped it up and sent it with a note saying, I love you, I meant it now, I know what a fool I've been but if you kissed me now I know you'd fool me again \
                Last Christmas, I gave you my heart But the very next day you gave it away This year, to save me from tears I'll give it to someone special"
        
        task_messages = [
            " Im Rewe angekommen wird es nicht besser. Lautstark dröhnt das Lied, welches keiner mehr hören kann, aus der Musikanlage." ,
            " Die Musik ist so laut, dass dein Kopf förmlich platzt. Und das schlimmste: der Ohrwurm ist garantiert. Daher begibst du dich " ,
            " sofort auf die Suche nach der Musikanlage, welche du hinter der Tiefkühltheke findest. Je näher du kommst, desto lauter dröhnt die Musik. " ,
            " Aufhören , schreist du die Musikanlage an, jedoch passiert nichts. Hätte ich bloß nicht so viel getrunken mit dem Langohrhasen, " ,
            " dann hätte ich auch sofort eine Idee gehabt, das Gerät auszustellen. Doch dann siehst du die Erlösung: um die Musik auszuschalten " ,
            " musst du lediglich einen Pin von 3 Zahlen eingeben. Easy denkst du. Doch wie kriegst du den Pin heraus? ",
            " Auf einem Zettel steht:<br><br><b>" + zettel + "<br><br>"
            
            "<br>Gesamt: Last Christmas I gave you my heart" , 
            " Binärzahl", 
            " Binärzahl komprimieren" , 
            " Alles klar, dann mal los!"
        ]
        hints = [
            "Zähle nach, wie oft welcher Buchstabe in dem Text, der auf dem Zettel steht, vorkommt" ,
            "Der Text beginnt mit Last und endet mit special" ,
            "Rechne die Anzahl der Zahlen, die sich hinter jedem einzelnen Buchstaben in diesem Satz Last Christmas I'll give you my heart zusammen" ,
            "Nun berechne aus der Dezimalzahl eine Binärzahl" ,
            "Dir fällt auf, dass der Pin aus 3 Zahlen besteht, die Binärzahl jedoch aus 9 Zahlen " ,
            "Komprimiere daher die Binärzahl ", 
            "Wichtig: Beginne vorne mit der 1 zu zählen " ,
            "Gib den dreistelligen Pin ein"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level1, "data": zettel}
        
    def create_level5(self):
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
             " Du läufst aus dem Rewe heraus und verdammt, schon wieder ein verschlossener Raum. Wie gewonnen so zerronnen. " 
            " Wann endet dieses Martyrium? Du schaust dich um und erkennst, dass du in einer Küche stehst. " 
            " Es ist ziemlich benebelt im Raum und du erkennst am Ende der Küche einen finsteren Reiter."
            " Der Reiter gibt dir einen Brief, den du entziffern musst. Auf dem Brief steht: <br><br><b>" + story + "<br><br>"
            "<br>Sobald du den Brief entzifferst und das Lösungswort vorliest, öffnet sich die Tür. "
        ]

        hints = [
            "Kommen dir bestimmte Begriffe nicht aus dem Schulunterricht bekannt vor? ", 
            "Es klingt wie Harry Potter, aber es hat nichts mit ihm zutun ",
            "Es gab ein Fach in der Schule, welches sich auf die oberen Elemente bezogen haben, "
            "Richtig, der Chemie-Unterricht ",
            "Du erkennst hier Abkürzungen für die Elemente, in englischer Sprache ",
            "Rein zufällig existiert auf Github eine CSV-Datei, die Elements.csv heißt " ,
            "Lies die csv-Datei ein ",
            "Versuche die Elemente durch die Abkuerzungen zu ersetzen ",
            "Anschließend kannst du den Text entschluesseln, sobald du die Abkuerzungen ersetzt hast",
            "Sobald du erkennst, wie der Pin sich zusammensetzt, musst du diesen auch noch beweisen ",
            "Dann mal los"

        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level2_translate, "data": story}
    ### SOLUTIONS ###

    def level3(self, zettel):
        dictionary = {}
    
        for words in zettel:
            dictionary[words.upper()] = dictionary.get(words.upper(),0) + 1

        sentence = "LASTCHRISTMAS"
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
    
    def level5_translate(self,story):
        new_text = ""
        liste = story.split(" ")
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
  