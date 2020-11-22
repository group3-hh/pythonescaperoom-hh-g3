liste = ['5663686e61','454255a547','5663666e61','5ac4e54e45','6adc4e4445','429c434b45','c45256a45','57d64c46c5','5a41484d65','4a4f1b4552','27d74c43c5','5a4f464542','46796e6573','64f6727065','4b7c49434b','624c49334b','666c67734b','505041545a','4bd6544562','1c414e5a45','4c454e5645','ebc4534947','4b6c495050','686c696666','6b6c616d6d','5a31554e53','5a61756e73','7a61756e73']

def run(liste):
    pot = 2
    count = 0
    erg = ""
    
    length = len(liste)
    
    while (len(str(1089**pot))) != length:
        pot +=1
    a = 1089**pot
    
    temp_list = [int(x) for x in str(a)]
    temp_length = len(temp_list)
    
    for i in range(length):
        for j in liste[i]:
            if count == temp_list[0]:
                erg = erg + str(j)
                count = 0
                del temp_list[0]
                break
            else:
                count = count + 1
    erg = bytes.fromhex(erg).decode('utf-8')[::-1]
    return erg
