def izracunaj(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Deljenje sa nulom")
        return a / b
    if op == "^":
        return a ** b
    raise ValueError("Nepoznata operacija")