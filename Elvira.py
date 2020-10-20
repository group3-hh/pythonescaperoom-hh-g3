import random
import string
from EscapeRoom import EscapeRoom


class Elvira(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Achim", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())

    ### LEVELS ###

    def create_level1(self):
        rechnung = random.choice([2 * 3, 2 * 3])

        task_messages = [
            "Mit brummenden Schädel erwachte der rot bemantelte Mann. Nie wieder den selbgepanschten Eierlikör des langorhigen schwor er sich",
            "Verdammt dunkel hier, wie war noch die Pin seines Handy? Wie ging noch das Lied dieser schwedische Pferde Besitzerin?"
        ]
        hints = [
            "2 x 3 macht 4 "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level1, "data": rechnung}

    def create_level2(self):
        spracher = random.choice(["alexa", "siri", "google"])

        task_messages = [
            "Ein wenig Licht, aber natürlich kein Empfang. Er war in einen kleinen Raum. In der Ecke stand so ein Spracherkennungsding",
            "Wie aktiviert man das Ding nochmal?"
        ]
        hints = [
            "Es ist nicht Alex "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level2, "data": spracher}

    def create_level3(self):
        numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
        task_messages = [
            "Der Lautsprecher begann zu leuchten und eine Stimme ertönte",
            f"Merke dir folgende Zahlen: <b> {numbers} </b "
            "Sie helfen dir die Tür, die mit einem Code verschlossen ist öffnen zu können.",
            "Ein Hinweis sei dir gegönnt: High and Low.",
            "Da der Kopf des bärtigen Herrn noch immer dröhnte legte er sich erst mal hin für ein kleines Nickerichen"
            "Nach einer nicht weiter definierten Zeit erwachte er wieder und im fiel sofort Panel zum eingeben des Codes auf"
            "und nach mehrmaligen Versuchen fällt ihm auf, dass du 2 verschiedene Codes eingeben musst.",
        ]

        hints = [
            "Was könnte High and Low mit den Zahlen zutun haben?",
            "Ist vielleicht die kleinste Zahl ein Code und die größte Zahl auch?"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level3, "data": numbers}

    ### SOLUTIONS ###

    def level1(self, rechnung):
        result = 2 * 3
        return result

    def level2(self, spracher):
        liste = ["alexa", "google", "siri"]
        search_for = spracher
        for result in liste:
            if result == search_for:
                return result

    def level3(self,numbers):

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