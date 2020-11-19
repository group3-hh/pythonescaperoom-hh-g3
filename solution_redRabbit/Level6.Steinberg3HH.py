import requests
import os
import sqlite3
import json

def run(name_choice):
    if load_database_from_web("https://pythonescaperoom.soeren-steinberg.de/alert.db") == True and os.path.exists("alert.db") and os.access("alert.db", os.R_OK):

        db = sqlite3.connect("alert.db")
        cursor = db.cursor()
        cursor.execute("SELECT firstname, lastname, securitycard_number, pin, active, date_of_expiry \
                        FROM securitycard_owner INNER JOIN securitycard on securitycard.sc_id = securitycard_owner.sc_id \
                        WHERE firstname = ? and active = 1 and date_of_expiry >= datetime('now')",(name_choice,))
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
    
def load_database_from_web(url):
    try:
        rq = requests.get(url)
        if rq.status_code == 200:
            open('alert.db', 'wb').write(rq.content)
            return True  
        else:
            return False
    except:
        print("Error - No connection!")