import random
import string
from EscapeRoom import EscapeRoom

class Elvira(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Achim", __name__)
        self.add_level(self.create_level1())



    ### LEVELS ###

    def create_level1(self):
        rechnung = random.choice([2 * 3 , 2 * 3 ])

        task_messages = [
            "Mit brummenden Schädel erwachte der rot bemantelte Mann. Nie wieder den selbgepanschten Eierlikör des langorhigen schwor er sich",
            "Verdammt dunkel hier, wie war noch die Pin seines Handy? Wie ging noch das Lied dieser schwedische Pferde Besitzerin?"
        ]
        hints = [
            "2 x 3 macht 4 "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.moblie_pin, "data": rechnung}
		
	

    ### SOLUTIONS ###

    def moblie_pin(self, rechnung):
        result = 2*3
        return result