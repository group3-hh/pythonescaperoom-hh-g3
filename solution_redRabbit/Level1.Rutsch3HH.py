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

    sum = a - int(b)
    if int(sum) <= 99:
        sum = int(sum) * 10
    b = str(sum)[::-1]
    erg = sum + int(b)
    return erg

