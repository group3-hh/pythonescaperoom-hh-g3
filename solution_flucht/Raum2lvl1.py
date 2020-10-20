def run(numbers):

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