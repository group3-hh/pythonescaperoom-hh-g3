def run(pw):
    spaces = [i for i, letter in enumerate(pw) if letter == " "]
    pw = list(pw)
    for i in range(len(spaces) - 1, -1, -1):
        pw.pop(spaces[i])
    srev = pw[::-1]
    for i in range(0, len(spaces)):
        srev.insert(spaces[i], " ")
    final = ""
    for z in srev:
        final = final + z
    return final

