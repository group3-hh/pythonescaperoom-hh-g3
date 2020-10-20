from EscapeRoom import EscapeRoom


class Raum2(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Tim", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level1(self):
        numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
        task_messages = [
            "Du triffst auf eine Tür, die mit einem Code verschlossen ist.",
            "Auf dem Eingabefeld für den Code steht: High and Low.",
            "Über der Tür entdeckst du mehrere Zahlen "
            "und nach mehrmaligen Versuchen fällt dir auf, dass du 2 verschiedene Codes eingeben musst.",
            f"Die Zahlen über der Tür sind folgende: <b> {numbers} </b ",
            "Am Besten schreibst du die Codes auf eine Liste, um Sie nicht zu vergessen"
        ]

        hints = [
            "Was könnte High and Low mit den Zahlen zutun haben?",
            "Ist vielleicht die kleinste Zahl ein Code und die größte Zahl auch?"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.high_low, "data": numbers}

    def create_level2(self):


    ### SOLUTIONS ###

    def high_low(self,numbers):

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
