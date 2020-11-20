import random
import string
from EscapeRoom import EscapeRoom

class Rewe(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Konsu", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###

    def create_level1(self):
        
        zettel = "Last Christmas, I gave you my heart but the very next day you gave it away . \
                This year, to save me from tears I'll give it to someone special. <br> Last Christmas, I gave you my heart but the very next day you gave it away. <br> This year, to save me from tears I'll give it to someone special . \
                <br> Once bitten and twice shy I keep my distance but you still catch my eye tell me, baby do you recognize me? \
                <br> Well, it's been a year It doesn't surprise me ( Merry Christmas ! )  \
                <br> I wrapped it up and sent it with a note saying, I love you, I meant it now, I know what a fool I've been but if you kissed me now I know you'd fool me again \
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

    ### SOLUTIONS ###

    def level1(self,zettel):
        dictionary = {}
    
        for words in zettel:
            dictionary[words.upper()] = dictionary.get(words.upper(),0) + 1

        sentence = "LASTCHRISTMAS"
        sum = 0
        for x in sentence:
            sum = sum + dictionary[x]
            #print(sum)
            binary = bin(sum)[2:]
            #print(binary)
            #print(compress(binary))
       
        return binary
    
    def level1(self,zahl):
        whole_number = 0
        first_number = 1
        finish_number = []
   
        for element in zahl:
            if element != first_number:
                finish_number.append(whole_number)
                whole_number = 0
            whole_number += 1
            first_number = element
        finish_number.append(whole_number) 
        return finish_number

    #level1(songtext)    