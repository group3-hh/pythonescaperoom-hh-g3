def run(num):
    liste = []
    final = []
    num = str(num)

    for i in range(0, len(num)):
        liste.append(num[i])

    for i in range(0, len(num)):
        final.append(int(liste[i]))
    result = sum(final)

    return result
