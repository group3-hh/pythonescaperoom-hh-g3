def run(meng):
     
    list1 = [i.split('SEPERATOR')[0] for i in meng]
    list2 = [i.split('SEPERATOR')[1] for i in meng]
    rezp = {}

    def create_liste(nliste,intr):
        pos = intr -1
        index = 0
        len_list = (len(nliste))
        temp1 = []
    
        for i in range(len_list):
        
            while len_list > 0:  
                index = (pos + index) % len_list
                temp1.append(nliste[index])
                nliste.pop(index)
                len_list = (len(nliste))
        return temp1
    
    menge = create_liste(list1,3)
    zutat = create_liste(list2,5)
    
    rezp = {zutat[i]: menge[i] for i in range(5)} 
    return rezp
