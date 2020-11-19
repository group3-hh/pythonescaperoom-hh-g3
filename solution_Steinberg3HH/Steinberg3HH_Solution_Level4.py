import json

def run(json_choice):
    json_deserialization = json.loads(json_choice)
    id_number = json_deserialization["identitycard"][0]["idnumber"]
    birth_date = json_deserialization["identitycard"][0]["birthdate"]
    expiry_date = json_deserialization["identitycard"][0]["expirydate"]
    total_check_number = json_deserialization["identitycard"][0]["totalchecknumber"]

    id_number_is_valid = calculate_checksum(id_number[:-1]) == int(id_number[-1])
    birth_date_is_valid = calculate_checksum(birth_date[:-1]) == int(birth_date[-1])
    expiry_date_is_valid = calculate_checksum(expiry_date[:-2]) == int(expiry_date[-2])

    cipher = str(id_number) + str(birth_date) + str(expiry_date[:-1])
    total_check_is_valid = calculate_checksum(cipher) == int(total_check_number)

    if id_number_is_valid == True and birth_date_is_valid == True and expiry_date_is_valid == True and total_check_is_valid == True:
        return True
    else:
        return False

def calculate_checksum(cipher):
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
