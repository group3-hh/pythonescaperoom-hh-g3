import random
import string
from EscapeRoom import EscapeRoom


class Elvira(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Achim", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

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
            "2 x 3 macht 4 "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level2, "data": spracher}

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
