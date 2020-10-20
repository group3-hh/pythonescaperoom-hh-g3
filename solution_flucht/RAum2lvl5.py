def run(code):
    code = str(code)
    code = code[:2] + "#" * (len(code) - 2)

    return code
