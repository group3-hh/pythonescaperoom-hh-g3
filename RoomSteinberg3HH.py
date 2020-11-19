import random
import string
import json
import requests
import os
import sqlite3
from EscapeRoom import EscapeRoom

run = 1

class RoomSteinberg3HH(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Sören", __name__)
        self.add_level(self.create_level4())
        self.add_level(self.create_level6())

    ### LEVELS ###
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
                "Dir gelingt es, die SQLight-Datenbank zu kopieren, die dir unter <b> https://pythonescaperoom.soeren-steinberg.de/alert.db </b> zur Verfügung steht.",
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
                "War ja nicht seine Schuld dass die Lagerhalle nebenan die Zugangsdaten offen im Internet unter <b>https://pythonescaperoom.soeren-steinberg.de/alert.db </b><br>",
                "stehen ließ. Mal schauen wer ihm heute den Zutritt gewährte. Anschließend musste er zwingend telefonieren und die Wogen glätten. Kartoffelsalat und Würstchen<br>",
                "waren quasi schon vorbereitet."
            ]
            hints = [
                "Könnte es die "+name_choice+" sein, die Zugang zur Lagerhalle hat?",
                "Denk daran, der Schnittstelle des Zutrittssystems die Daten wieder als JSON-Objekt mit den Eigenschaftsnamen "
                "firstname, lastname, securitycard_number und pin zu übergeben"
            ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.level6_crack_authorization, "data": name_choice}

    ### SOLUTIONS ###

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
                '1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0',
                'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'18',
                'J':'19','K':'20','L':'21','M':'22','N':'23','O':'24','P':'25','Q':'26','R':'27',
                'S':'28','T':'29','U':'30','V':'31','W':'32','X':'33','Y':'34','Z':'35'
            }

            position = 1
            sum = 0
            multiply7 = [x for x in range(1,40,3)]
            multiply3 = [x for x in range(2,40,3)]
            multiply1 = [x for x in range(3,40,3)]

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
    
    def level6_crack_authorization(self, name_choice):
        if self.level6_load_database_from_web("https://pythonescaperoom.soeren-steinberg.de/alert.db") == True and os.path.exists("alert.db") and os.access("alert.db", os.R_OK):

            db = sqlite3.connect("alert.db")
            cursor = db.cursor()
            cursor.execute("SELECT firstname, lastname, securitycard_number, pin, active, date_of_expiry FROM securitycard_owner INNER JOIN securitycard on securitycard.sc_id = securitycard_owner.sc_id WHERE firstname = ? and active = 1 and date_of_expiry >= datetime('now')",(name_choice,))
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