from EscapeRoom import EscapeRoom


class FluchtVorDemCode(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Tim", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())
        self.add_level(self.create_level4())
        self.add_level(self.create_level5())
        self.add_level(self.create_level6())

    ### LEVELS ###

    def create_level1(self):
        numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
        task_messages = [
            "Du triffst auf eine Tür, die mit einem Code verschlossen ist.",
            "Auf dem Eingabefeld für den Code steht: High and Low.",
            "Über der Tür entdeckst du mehrere Zahlen "
            "und nach mehrmaligen Versuchen fällt dir auf, dass du 2 verschiedene Codes eingeben musst.",
            f"Die Zahlen über der Tür sind folgende: <b> {numbers} </b ",
            "Am besten schreibst du die Codes auf eine Liste, um Sie nicht zu vergessen"
        ]

        hints = [
            "Was könnte High and Low mit den Zahlen zutun haben?",
            "Ist vielleicht die kleinste Zahl ein Code und die größte Zahl auch?",
            "Gib die Codes als Liste wieder"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.high_low, "data": numbers}

    def create_level2(self):
        num = 542
        task_messages = [
            "Die Tür hat sich geöffnet und einen Gang offenbart. Du gehst den Gang entlang und nach einiger Zeit "
            "kommst du an eine Gabelung mit 2 weiteren Gängen.",
            "Über jedem Gang steht eine Zahl, jedoch gibt es keinen weiteren Hinweis. Vielleicht kann dir ja eine "
            "Zahl von der Liste helfen, die du noch von vorhin hast.",
            "<b> Über dem linken Gang steht die Zahl 11 </b",
            "<b> Über dem mittleren Gang steht die Zahl 8 </b",
            "<b> Über dem rechten Gang steht die Zahl 2 </b",
            "Du musst dich für eine Zahl entscheiden"
        ]
        hints = [
            "Die Zahlen, die auf deiner Liste stehen, sind: -214 und 542",
            "Du musst dich auf die höhere Zahl deiner Liste konzentrieren",
            "Es gibt einen Zusammenhang zwischen der 542 und der Zahl von einem Gang",
            "Du musst die Quersumme von 542 berechnen",
            "Gib diese als Integer wieder"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.qs, "data": num}

    def create_level3(self):
        chars = "joouqqnmmi"
        task_messages = [
            "Du hast den richtigen Gang gewählt und findest eine antike Steintafel und ""einen Kalender.",
            " Du kannst erkennen, dass verschiedene Buchstaben in diese Steintafel gemeißelt sind.",
            f"Die Buchstaben auf der Steintafel sind folgende: <b> {chars} </b",
        ]
        hints = [
            "Gucke dir an, wie oft es welchen Buchstaben gibt",
            "Gucke dir die Buchstaben an, die sich nicht wiederholen",
            "Gib diese als String wieder"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.fnr, "data": chars}

    def create_level4(self):
        rnglow = 2
        rnghigh = 30
        task_messages = [
            "Du suchst den Monat Juni und siehst, dass auf der Seite in großer roter Schrift,"
            " -Primzahlen- geschrieben steht.",
            "Der Juni hat insgesamt 30 Tage, jedoch ist der 1. Juni durchgestrichen.",
            f"<b> Es sind also nur die Tage von {rnglow} bis {rnghigh} in dem Kalender</b",
            "Du solltest deine Ergebnisse wohl besser wieder auf eine Liste schreiben",
            "<b> Anmerkung:</b",
            "Du bekommst als Input die Obergrenze, (also 30). Das bedeutet, dass du die Untergrenze (also 2) selber "
            "definieren musst "
        ]
        hints = [
            "Finde die Primzahlen zwischen 2 und 30",
            "Gib die Primzahlen als Liste wieder"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.prim, "data": rnghigh}

    def create_level5(self):
        code = 192329
        task_messages = [
            "Du schaust dich in dem Raum noch ein wenig um und mit einmal entdeckst du einen Tresor, welcher auch "
            "mit einem Code gesichert ist.",
            "Du sollst die letzten 3 Primzahlen als Code eingeben, jedoch sollen die"
            "letzten 4 Ziffern maskiert sein.",
            "<b> Beispiel:</b",
            "24####"
        ]

        hints = [
            "Die Primzahlen von vorhin waren: <b> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29</b",
            "Gib den Code als String wieder"
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.mask, "data": code}

    def create_level6(self):
        pw = "Vielen Dank, dass du diesen Escape Room gespielt hast, ich hoffe es hat Spaß gemacht"

        task_messages = [

            "Du bist nun vor der letzten Tür und dir fehlt nur noch ein ein Passwort, um zu entkommen.",
            "An einer Wand steht ein Beispiel, nach welchem Schema du auch gleich vorgehen musst.",
            "<b> Du Hast es gleich geschafft!  -  !t ffah cs eghcie lgsetsaHuD</b",
            "Nach diesem Schema musst du jetzt den Passwortsatz herausfinden. Dein gegebener Satz ist:",
            f"<b> {pw}</b"
        ]

        hints = [
            "Probiere den Satz rückwärts zu lesen",
            "Achte auf die Leerzeichen",
            "Du musst den Satz umdrehen, aber die Leerzeichen müssen an derselben Stelle bleiben",
            "Gib das Passwort als String wieder"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.revsp, "data": pw}

    ### SOLUTIONS ###

    def high_low(self, numbers):

        x = []
        v = []
        k = []
        y = numbers.split(" ")

        for i in range(0, len(y)):
            v.append(int(y[i]))

        v.sort()
        x.append(v[len(v) - 1])
        x.append(v[0])

        for i in range(0, len(x)):
            k.append(x[i])

        result = k

        return result

    def qs(self, num):
        liste = []
        final = []
        num = str(num)

        for i in range(0, len(num)):
            liste.append(num[i])

        for i in range(0, len(num)):
            final.append(int(liste[i]))
        result = sum(final)

        return result

    def fnr(self, chars):
        testlist = []
        charlist = list(chars)
        final = []
        print(len(charlist))

        for i in range(0, len(charlist)):
            print(testlist)
            testlist.append(charlist[i])
            charlist.pop(i)
            if testlist[0] not in charlist:
                final.append(testlist[0])
                charlist.insert(i, testlist[0])
                testlist = []
            else:
                charlist.insert(i, testlist[0])
                testlist = []

        result = "".join(final)

        return result

    def prim(self, rnghigh):
        rnglow = 2
        result = []
        for num in range(rnglow, rnghigh):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result.append(num)

        return result

    def mask(self, code):
        code = str(code)
        result = code[:2] + "#" * (len(code) - 2)

        return result

    def revsp(self, pw):
        spaces = [i for i, letter in enumerate(pw) if letter == " "]
        pw = list(pw)
        for i in range(len(spaces) - 1, -1, -1):
            pw.pop(spaces[i])
        srev = pw[::-1]
        for i in range(0, len(spaces)):
            srev.insert(spaces[i], " ")
        final = ""
        for z in srev:
            final = final + z
        return final
