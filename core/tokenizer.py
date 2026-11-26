OPERATORS = ["+", "-", "*", "/", "(", ")"]


def tokenize(expression):
    tokens = []
    number = ""

    for char in expression:
        if char.isdigit() or char == ".":
            number += char
        else:
            if number:
                tokens.append(float(number))
                number = ""

            if char in OPERATORS:
                tokens.append(char)
            elif char != " ":
                raise ValueError(f"Invalid character: {char}")

    if number:
        tokens.append(float(number))

    if not tokens:
        raise ValueError("Empty expression")

    return tokens
