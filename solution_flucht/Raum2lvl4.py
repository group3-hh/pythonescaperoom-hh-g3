def run(rnghigh):
    final = []
    for num in range(2, rnghigh):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            final.append(num)

    return final
