def run(numbers):
    counter = 0
    numbers.sort(reverse=True)
    numbers = [x for x in numbers if x % 2 == 0]
    a = numbers[counter]
    b = str(a)[::-1]

    while a > 998 or a < 100 or a <= int(b):
        counter += 1
        a = numbers[counter]
        b = str(a)[::-1]

    diff = a - int(b)
    if int(diff) <= 99:
        diff = int(diff) * 10
    b = str(diff)[::-1]
    erg = diff + int(b)
    return erg

