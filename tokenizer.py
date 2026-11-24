OPERATORS = ['+', '-', '*', '/', '(', ')']

def tokenize(expression):
    tokens = []
    number = ''  # digits collected so far

    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        else:
            # a number just ended, so save it
            if number:
                tokens.append(float(number))
                number = ''

            if char in OPERATORS:
                tokens.append(char)
            elif char != ' ':
                raise ValueError(f'Invalid character: {char}')

    # the expression may end with a number
    if number:
        tokens.append(float(number))

    if not tokens:
        raise ValueError('Empty expression')
    return tokens